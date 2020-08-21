workflow simple_wf {
    call simple_task
    output {
      Array[File] out = simple_task.out
    }
}

task simple_task {


  command <<<
    touch out.vcf
    touch out.bam
  >>>

  output {
     Array[File] out= ["out.vcf", "out.bam"]
  }
}
