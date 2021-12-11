package com.jerome.wordcount.component;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

/**
 * 自定义 partitioner，按照单词分区
 */

public class CustomPartitioner extends Partitioner<Text, IntWritable> {

    @Override
    public int getPartition(Text key, IntWritable value, int numPartitions) {
        if (key.toString().equals("Azkaban")) {
            return 0;
        }else if (key.toString().equals("Flink")) {
            return 1;
        }else if (key.toString().equals("Flume")) {
            return 2;
        }else if (key.toString().equals("HBase")) {
            return 3;
        }else if (key.toString().equals("Hadoop")) {
            return 4;
        }else if (key.toString().equals("Hive")) {
            return 5;
        }else if (key.toString().equals("Kafka")) {
            return 6;
        }else if (key.toString().equals("Kudu")) {
            return 7;
        }else if (key.toString().equals("Presto")) {
            return 8;
        }else if (key.toString().equals("Spark")) {
            return 9;
        }else if (key.toString().equals("Storm")) {
            return 10;
        }else {
            return 11;
        }
    }
}
