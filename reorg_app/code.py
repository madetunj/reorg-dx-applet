import json

import dxpy

@dxpy.entry_point('main')
def main(reorg_conf___=None, reorg_status___=None):

    # download and parse `reorg_conf___`
    #conf_file = dxpy.DXFile(reorg_conf___)

    #dxpy.download_dxfile(conf_file.get_id(), "conf.json")

    #with open('conf.json') as f:
    #    conf = json.load(f)

    # find the output stage of the current analysis


    analysis_id = dxpy.describe(dxpy.JOB_ID)["analysis"]


    stages = dxpy.describe(analysis_id)["stages"]


    # retrieve the dictionary containing outputs, where key is the name of output and value is the link to the file.
    output_map = [x['execution']['output'] for x in stages if x['id'] == 'stage-outputs'][0]

    out = output_map['out']

    bam = [x for x in out if dxpy.describe(x)["name"].endswith('.bam')][0]
    vcf = [x for x in out if dxpy.describe(x)["name"].endswith('.vcf')][0]

    vcf_folder = "/results/out/vcf" #conf['vcf']
    bam_folder = "/results/out/bam" #conf['bam']

    # get the container instance
    dx_container = dxpy.DXProject(dxpy.PROJECT_CONTEXT_ID)

    dx_container.new_folder(vcf_folder,parents=True)
    dx_container.new_folder(bam_folder,parents=True)

    dx_container.move(
        destination=vcf_folder,
        objects=[ vcf['$dnanexus_link'] ]
    )
    dx_container.move(
        destination=bam_folder,
        objects=[ bam['$dnanexus_link'] ],
    )

