import java.io.IOException;
import java.io.PrintStream;
import java.util.HashMap;
import java.util.Map;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Mapper.Context;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
public class BusyMonth

{
    public BusyMonth() {}

    public static class TokenizerMapper
            extends Mapper<Object, Text, Text, IntWritable>
    {
        private Text word = new Text();

        public TokenizerMapper() {}
        public void map(Object paramObject, Text paramText, Mapper<Object, Text, Text, IntWritable>.Context paramMapper) throws IOException, InterruptedException { HashMap localHashMap = new HashMap();
            
            String str1 = paramText.toString();
            String[] arrayOfString1 = str1.split(",");
            String[] arrayOfString_date = arrayOfString1[1].split("/");
	    String str_date_time = arrayOfString_date[0]+"/" + arrayOfString_date[2];
	    String[] arrayOfString_date_time = str_date_time.split(" ");
	    String str_date = arrayOfString_date_time[0];
	    		   
	   Text key = new Text();
           Text record = new Text();
           IntWritable  val = new IntWritable(Integer.parseInt(arrayOfString1[5]));

                if((arrayOfString1[2].equals("Terminal 1")|arrayOfString1[2].equals("Terminal 2")|arrayOfString1[2].equals("Terminal 3")|arrayOfString1[2].equals("Terminal 4")|arrayOfString1[2].equals("Terminal 5")|arrayOfString1[2].equals("Terminal 6")|arrayOfString1[2].equals("Terminal 7")|arrayOfString1[2].equals("Tom Bradley International Terminal")|arrayOfString1[2].equals("Terminal 8")))
                {
                   key.set(str_date);
		   paramMapper.write(key,val);
	          // System.out.println(key+ "+" + val);
                }

        }
    }

    public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable>
    {
        private IntWritable result = new IntWritable();

        public IntSumReducer() {}

        public void reduce(Text paramText, Iterable<IntWritable> paramIterable, Reducer<Text, IntWritable, Text, IntWritable>.Context paramReducer) throws IOException, InterruptedException
        {
            int i = 0;

            for ( IntWritable str : paramIterable)
            {
                    i+= str.get();
            
            if(i>5000000)
		{	
			result.set(i);

		}
	    else
		{
			result.set(0);
		}
	}
           if(result.get() != 0 )
	{
		
		//String res_key = paramText.toString();
		//String startDateString = res_key;
		//DateFormat df = new SimpleDateFormat("MM/yyyy"); 
		//Date startDate = new Date();
    		//String newDateString = df.format(startDate);
    		//System.out.println(newDateString);

		//Text paramText2 = new Text(newDateString);
		 paramReducer.write(paramText,result);
	}
        }
    }
    public static void main(String[] paramArrayOfString) throws Exception
    {
        Configuration localConfiguration = new Configuration();
        String[] arrayOfString = new GenericOptionsParser(localConfiguration, paramArrayOfString).getRemainingArgs();
        if (arrayOfString.length < 2) {
            System.err.println("Usage: wordcount <in> [<in>...] <out>");
            System.exit(2);
        }
        Job localJob = Job.getInstance(localConfiguration, "busy month");
        localJob.setJarByClass(BusyMonth.class);
        localJob.setMapperClass(BusyMonth.TokenizerMapper.class);
        localJob.setCombinerClass(BusyMonth.IntSumReducer.class);
        localJob.setReducerClass(BusyMonth.IntSumReducer.class);
        localJob.setOutputKeyClass(Text.class);
        localJob.setOutputValueClass(IntWritable.class);
        for (int i = 0; i < arrayOfString.length - 1; i++) {
            FileInputFormat.addInputPath(localJob, new Path(arrayOfString[i]));
        }
        FileOutputFormat.setOutputPath(localJob, new Path(arrayOfString[(arrayOfString.length - 1)]));

        System.exit(localJob.waitForCompletion(true) ? 0 : 1);
    }
}


