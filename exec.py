from phaseA import sort_array, count_weekday_occurrences, write_recent_first_lines, create_data, format_data, extract_sender_email, generate_markdown_index,card_ocr,similar_comments,sql_query
from phaseB import fetch_api,clone_repo,run_query,scrape,comp_resize_image,transcribe_audio
def execute(func,args):
    if func=='sort_array':
        sort_array(args['input_file'],args['first_target'],args['second_target'],args['output_file'])
    elif func=='count_weekday_occurrences':
        count_weekday_occurrences(args['input_file'],args['output_file'],args['target_day'])
    elif func=='write_recent_first_lines':
        write_recent_first_lines(args['input_dir'],args['output_file'],args['num_files'])
    elif func=='create_data':
        create_data(args['path'],args['email'])
    elif func=='format_data':
        format_data(args['path'],args['version'])
    elif func=='extract_sender_email':
        extract_sender_email(args['inputfile'],args['outputfile'])
    elif func=='generate_markdown_index':
        generate_markdown_index(args['directory'],args['output_file'])
    elif func=='card_ocr':
        card_ocr(args['inputimage'],args['outputfile'])
    elif func=='similar_comments':
        similar_comments(args['inputfile'],args['outputfile'])
    elif func=='sql_query':
        sql_query(args['database'],args['table'],args['type'],args['outputfile'])
    elif func=='fetch_api':
        fetch_api(args['url'],args['parameters'],args['save_path'])
    elif func=='clone_repo':
        clone_repo(args['url'])
    elif func=='run_query':
        run_query(args['query'],args['database'],args['db_type'])
    elif func=='scrape':
        scrape(args['url'],args['file_path'])
    elif func=='comp_resize_image':
        comp_resize_image(args['inputfile'],args['outputfile'])
    elif func=='transcribe_audio':
        transcribe_audio(args['mp3_path'],args['outputfile'])