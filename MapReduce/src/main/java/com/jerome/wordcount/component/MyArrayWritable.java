package com.jerome.wordcount.component;

import org.apache.hadoop.io.ArrayWritable;
import org.apache.hadoop.io.Text;


public class MyArrayWritable extends ArrayWritable { 
	public MyArrayWritable() { 
		super(Text.class);
	} 
	
	public MyArrayWritable(String[] strings) {
		super(strings); 
	} 

}

