package com.jerome.wordcount;
import com.jerome.wordcount.component.MyArrayWritable;
import com.jerome.wordcount.component.WordCountMapper;
import com.jerome.wordcount.component.WordCountReducer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

/**
 * 打包 jar 到集群使用 hadoop 命令提交作业
 *
 * creat_date: 2021/09/03
 * creat_time: 上午10:30
 */

public class WordCountApp {
    public static void main(String[] args) throws Exception {

        Configuration configuration = new Configuration();
        
        // 2、获取 job 对象
        Job job = Job.getInstance(configuration,"wordcount");

        // 3、设置 jar 存储位置
        job.setJarByClass(WordCountApp.class);

        // 4、关联 Mapper 和 Reducer
        job.setMapperClass(WordCountMapper.class);
        job.setReducerClass(WordCountReducer.class);

        // 设置 Reduce 个数
        //job.setNumReduceTasks(1);

        // 5、设置 Mapper 阶段输出数据的 key 和 value 类型
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(MyArrayWritable.class);

        // 6、设置 Reducer 阶段输出数据的 key 和 value 类型
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(DoubleWritable.class);

        // 7、如果输出目录已经存在，则必须先删除，否则重复运行程序时会抛出异常
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        // 9、提交 job 到群集并等待它完成，参数设置为 true 代表打印显示对应的进度
        boolean b = job.waitForCompletion(true);

        if (!b){
          System.out.println("word count failed!");
        }
    }
}