package com.jerome.wordcount.component;

import java.io.IOException;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

/**
 * 在 Reduce 中进行单词出现次数的统计

 * Text         : Mapping 输入的 key 的类型
 * IntWritable  : Mapping 输入的 value 的类型
 * Text         : Reducing 输出的 key 的类型
 * IntWritable  : Reducing 输出的 value 的类型
 */

public class WordCountReducer extends Reducer<Text, MyArrayWritable, Text, DoubleWritable> {

    @Override
    protected void reduce(Text key, Iterable<MyArrayWritable> values, Context context) throws IOException, InterruptedException {
    	int lettercounter = 0;
        int wordcounter = 0;
        int sentencecounter = 0;
        String[] arr=new String[3];   
        double ColemanLiauIndexScore;
        double L;
        double S;
        for (MyArrayWritable value : values) {
        	arr = value.toStrings();
            lettercounter = Integer.parseInt(arr[0].trim());
            sentencecounter = Integer.parseInt(arr[1].trim());
            wordcounter = Integer.parseInt(arr[2].trim());
        }
        //calculate the CLI
        if (wordcounter ==0) {
        	ColemanLiauIndexScore =0;
        }else {
        	L = lettercounter * 100 / wordcounter;
        	S = sentencecounter * 100 / wordcounter;
        	ColemanLiauIndexScore = (0.0588 * L - 0.296 * S - 15.8);
        }
     
        // output <Id:CLI> key-value
        context.write(key, new DoubleWritable(ColemanLiauIndexScore));
    }
}
