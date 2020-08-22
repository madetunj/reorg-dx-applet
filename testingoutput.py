import json

import dxpy

#@dxpy.entry_point('main')

def main(): 
    #reorg_conf___=None, reorg_status___=None):

    # download and parse `reorg_conf___`
    conf_file = dxpy.DXFile('file-Fvy5zQ89pQvPXqJk86X6Bbbk')
    #print(conf_file.get_id())

    dxpy.download_dxfile(conf_file.get_id(), "conf.json")

    with open('conf.json') as f:
        conf = json.load(f)

    # find the output stage of the current analysis

    #job_id is reorg_app:main
#    job = "job-FvqFQbQ9Q65yGKz0J2Kvkfz8"
#    job = "job-FvqBp189Q65p0YG54GPgJXXP"
#    job = "job-Fvy60409pQvBFG9Z6z0bx3Q7"
#    analysis_id = dxpy.describe(job)["analysis"]

    #analysis_id = "analysis-Fx00JJ09J273vqQb8P8B78z0" #SEASEQ-4-glob
    analysis_id = "analysis-Fx02fK095JG3Pyb4BgQJj4Yz" #SEASEQ-5-motifs

    #print(dxpy.describe(job))

    #print(analysis_id, "analysis_id")

    stages = dxpy.describe(analysis_id)["stages"]

#    print (stages,"stages")

    # retrieve the dictionary containing outputs, where key is the name of output and value is the link to the file.
    output_map = [x['execution']['output'] for x in stages if x['id'] == 'stage-outputs'][0]
    folder_location = [x['execution']['folder'] for x in stages if x['id'] == 'stage-outputs'][0]

    dx_container = dxpy.DXProject(dxpy.PROJECT_CONTEXT_ID)

#FASTQC
    htmlfile = output_map['htmlfile']
    zipfile = output_map['zipfile']
    bam_htmlfile = output_map['bam_htmlfile']
    bam_zipfile = output_map['bam_zipfile']

    sample_name = dxpy.describe(htmlfile)["name"].split('_fastqc.html')[0]

    folder = "/output_files/" + sample_name + "/QC_files/FASTQC"
    dx_container.new_folder(folder,parents=True)
    for thestring in (htmlfile, zipfile, bam_htmlfile, bam_zipfile):
        if thestring is not None :
            dx_container.move(
                destination=folder,
                objects=[ thestring['$dnanexus_link'] ]
            )

#BASICMETRICS
    metrics_out = output_map['metrics_out']

#QC-STATS
    qc_statsfile = output_map['qc_statsfile']
    qc_htmlfile = output_map['qc_htmlfile']
    qc_textfile = output_map['qc_textfile']

    folder = "/output_files/" + sample_name + "/QC_files/STATS"
    dx_container.new_folder(folder,parents=True)
    for thestring in (metrics_out, qc_statsfile, qc_htmlfile, qc_textfile):
        if thestring is not None :
            dx_container.move(
                destination=folder,
                objects=[ thestring['$dnanexus_link'] ]
            )

#FLANKBED
    flankbedfile = output_map['flankbedfile']

#BAMFILES
    sortedbam = output_map['sortedbam']
    mkdupbam = output_map['mkdupbam']
    bklistbam = output_map['bklistbam']
    indexbam = output_map['indexbam']
    bklist_indexbam = output_map['bklist_indexbam']
    mkdup_indexbam = output_map['mkdup_indexbam']

    folder = "/output_files/" + sample_name + "/QC_files/STATS"
    dx_container.new_folder(folder,parents=True)
    for thestring in (sortedbam, mkdupbam, bklistbam, indexbam, bklist_indexbam, mkdup_indexbam):
        if thestring is not None :
            dx_container.move(
                destination=folder,
                objects=[ thestring['$dnanexus_link'] ]
            )

#MACS
    peakbedfile = output_map['peakbedfile']
    peakxlsfile = output_map['peakxlsfile']
    summitsfile = output_map['summitsfile']
    wigfile = output_map['wigfile']
    all_peakbedfile = output_map['all_peakbedfile']
    all_peakxlsfile = output_map['all_peakxlsfile']
    all_summitsfile = output_map['all_summitsfile']
    all_wigfile = output_map['all_wigfile']
    nm_peakbedfile = output_map['nm_peakbedfile']
    nm_peakxlsfile = output_map['nm_peakxlsfile']
    nm_summitsfile = output_map['nm_summitsfile']
    nm_wigfile = output_map['nm_wigfile']

    prefix_peaks_folder = "/output_files/" + sample_name + "/PEAKS_files"
    folder = prefix_peaks_folder + "/NARROW_peaks"
    dx_container.new_folder(folder,parents=True)
    for thestring in (peakbedfile, peakxlsfile, summitsfile, wigfile, all_peakbedfile, all_peakxlsfile, all_summitsfile, all_wigfile, nm_peakbedfile, nm_peakxlsfile, nm_summitsfile, nm_wigfile):
        if thestring is not None :
            dx_container.move(
                destination=folder,
                objects=[ thestring['$dnanexus_link'] ]
            )

#SICER
    scoreisland = output_map['scoreisland']
    sicer_wigfile = output_map['sicer_wigfile']

    folder = prefix_peaks_folder + "/BROAD_peaks"
    dx_container.new_folder(folder,parents=True)
    for thestring in (scoreisland, sicer_wigfile):
        if thestring is not None :
            dx_container.move(
                destination=folder,
                objects=[ thestring['$dnanexus_link'] ]
            )

#ROSE
    pngfile = output_map['pngfile']
    mapped_union = output_map['mapped_union']
    mapped_stitch = output_map['mapped_stitch']
    enhancers = output_map['enhancers']
    super_enhancers = output_map['super_enhancers']
    gff_file = output_map['gff_file']
    gff_union = output_map['gff_union']
    union_enhancers = output_map['union_enhancers']
    stitch_enhancers = output_map['stitch_enhancers']
    e_to_g_enhancers = output_map['e_to_g_enhancers']
    g_to_e_enhancers = output_map['g_to_e_enhancers']
    e_to_g_super_enhancers = output_map['e_to_g_super_enhancers']
    g_to_e_super_enhancers = output_map['g_to_e_super_enhancers']

    folder = prefix_peaks_folder + "/STITCHED_REGIONS"
    dx_container.new_folder(folder,parents=True)
    for thestring in (pngfile, mapped_union, mapped_stitch, enhancers, super_enhancers, gff_file, gff_union, union_enhancers, stitch_enhancers, e_to_g_enhancers, e_to_g_super_enhancers, g_to_e_enhancers, g_to_e_super_enhancers):
        if thestring is not None :
            dx_container.move(
                destination=folder,
                objects=[ thestring['$dnanexus_link'] ]
            )

#MOTIFS
    ame_tsv = output_map['ame_tsv']
    ame_html = output_map['ame_html']
    ame_seq = output_map['ame_seq']
    meme = output_map['meme']
    summit_ame_tsv = output_map['summit_ame_tsv']
    summit_ame_html = output_map['summit_ame_html']
    summit_ame_seq = output_map['summit_ame_seq']
    summit_meme = output_map['summit_meme']

#BAM2GFF
    m_downstream = output_map['m_downstream']
    m_upstream = output_map['m_upstream']
    m_genebody = output_map['m_genebody']
    m_promoters = output_map['m_promoters']
    pdf_gene = output_map['pdf_gene']
    pdf_h_gene = output_map['pdf_h_gene']
    png_h_gene = output_map['png_h_gene']
    pdf_h_gene = output_map['pdf_h_gene']
    pdf_promoters = output_map['pdf_promoters']
    pdf_h_promoters = output_map['pdf_h_promoters']
    png_h_promoters = output_map['png_h_promoters']

#VISUALIZATION
    bigwig = output_map['bigwig']
    norm_wig = output_map['norm_wig']
    tdffile = output_map['tdffile']
    n_bigwig = output_map['n_bigwig']
    n_norm_wig = output_map['n_norm_wig']
    n_tdffile = output_map['n_tdffile']
    a_bigwig = output_map['a_bigwig']
    a_norm_wig = output_map['a_norm_wig']
    a_tdffile = output_map['a_tdffile']



    #print(dxpy.describe(norm_wig)["name"])

#    folder = "/temporary"
    # get the container instance
#    dx_container = dxpy.DXProject(dxpy.PROJECT_CONTEXT_ID)

#    dx_container.new_folder(folder,parents=True)
#    for thegroup in output_map:
#        thegroup_path = output_map[thegroup]
#        #print(thegroup, thegroup_path)
#        if thegroup_path is not None :
#            dx_container.move(
#                destination=folder,
#                objects=[ thegroup_path['$dnanexus_link'] ]
#            )

#    dx_container.remove_folder(folder=folder_location, recurse=True)

#    for ccc in dx_container.list_folder(folder_location)['objects']:
#        print(ccc,ccc['id'])
#        dx_container.remove_objects(ccc)
#        print(ccc['id'])


#    dx_container.new_folder(bam_folder,parents=True)
#    dx_container.move(
#        destination=vcf_folder,
#        objects=[ vcf['$dnanexus_link'] ]
#    )
    #dx_container.move(
     #   objects=bam_folder,
      #  destination=[ bam['$dnanexus_link'] ],
    #)


if __name__ == "__main__":
    main()
