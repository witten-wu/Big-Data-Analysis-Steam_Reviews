package com.jerome.wordcount.component;

import java.io.IOException;
import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

/**
 * 将每行数据按照分隔符(" \t\n\r\f")进行拆分

 * Object      : Mapping 输入文件的内容
 * Text        : Mapping 输入的每一行的数据
 * Text        : Mapping 输出 key 的类型
 * IntWritable : Mapping 输出 value 的类型
 *
 */

public class WordCountMapper extends Mapper<Object, Text, Text, MyArrayWritable> {

    @Override
    protected void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        // get the value of each lines
        String line = value.toString();
        // Split the contents of this line into an array of words by space
        String[] words = StringUtils.split(line, ",");
        int len = words.length -1;
        String review = words[len];
        int Lengthofreview = review.length();
        String rewId = words[1];
        int lettercounter = 0;
        int wordcounter = 0;
        int sentencecounter = 0;
        for(int i=0;i<Lengthofreview;i++){
        	char ch = review.charAt(i);
        	if(Character.isLetter(ch)) {
        		lettercounter += 1;
        	}else if (ch == ' ') {
        		wordcounter += 1;
        	}else if (ch == '.' || ch=='?' || ch=='!') {
        		sentencecounter += 1;
        	}
        }
        if (wordcounter == 0 && lettercounter != 0){
            wordcounter = 1; 
    	}
        String[] arr=new String[3];    
        arr[0] = Integer.toString(lettercounter);
        arr[1] = Integer.toString(sentencecounter);;
        arr[2] = Integer.toString(wordcounter);;
        
        // Iterate over the output <key, value> key-value pairs
        context.write(new Text(rewId), new MyArrayWritable(arr));
    }
}
