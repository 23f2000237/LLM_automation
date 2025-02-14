funtion_tools=[
    {
        "type": "function",
        "function":{  
        "name":"create_data",
        "description": "This function will take the input path for a python file and an email address as input and run the file using the uv command",
        "parameters":{
            "type":"object",
            "properties":{
                "path":{
                    "type":"string",
                    "description":"The path to the python file"
                },
                "email":{
                    "type":"string",
                    "description":"The email address in the prompt"
                }
        },
        "additionalProperties": False,
        "required": ["path","email"]
        }
        }
    },
    {
        "type": "function",
        "function":{ 
        "name":"format_data",
        "description": "This function will take the input path for a python file and a version number as input and format the file using the prettier command",
        "parameters":{
            "type":"object",
            "properties":{
                "path":{
                    "type":"string",
                    "description":"The path to the python file"
                },
                "version":{
                    "type":"string",
                    "description":"The version number in the prompt"
                }
        },
        "additionalProperties": False,
        "required": ["path","version"]
        }
        }
    },
    {
        "type": "function",
        "function":{ 
        "name":"count_weekday_occurrences",
        "description": "This function will take the input file path, output file path, and target day as input and count the occurrences of the target weekday in the input file",
        "parameters":{
            "type":"object",
            "properties":{
                "input_file":{
                    "type":"string",
                    "description":"The path to the input file"
                },
                "output_file":{
                    "type":"string",
                    "description":"The path to the output file"
                },
                "target_day":{
                    "type":"string",
                    "description":"The target day in the prompt"
                }
        },
        "additionalProperties": False,
        "required": ["input_file","output_file","target_day"]
        }
        }
    },
    {
        "type": "function",
        "function":{ 
        "name":"sort_array",
        "description": "This function will take the input file path, first target, second target, and output file path as input and sort the array of contacts by the first and second target",
        "parameters":{
            "type":"object",
            "properties":{
                "input_file":{
                    "type":"string",
                    "description":"The path to the input file"
                },
                "first_target":{
                    "type":"string",
                    "description":"The first target in the prompt"
                },
                "second_target":{
                    "type":"string",
                    "description":"The second target in the prompt"
                },
                "output_file":{
                    "type":"string",
                    "description":"The path to the output file"
                }
        },
        "additionalProperties": False,
        "required": ["input_file","first_target","secomd_target","output_file"]
        }
        }
    },
    {
        "type": "function",
        "function":{
        "name":"write_recent_first_lines",
        "description": "This function will take the input directory path, output file path, and number of files as input and write the first line of the most recent files in the directory to the output file",
        "parameters":{
            "type":"object",
            "properties":{
                "input_dir":{
                    "type":"string",
                    "description":"The path to the input directory"
                },
                "output_file":{
                    "type":"string",
                    "description":"The path to the output file"
                },
                "num_files":{
                    "type":"integer",
                    "description":"The number of files in the prompt"
                }
        },
        "additionalProperties": False,
        "required": ["input_dir","output_file","num_files"]
        }
        }
    },
    {
    "type": "function",
    "function":{
    "name": "extract_sender_email",
    "description": "Extracts the sender's email from an input file and writes it to an output file.",
    "parameters": {
        "type": "object",
        "properties": {
            "inputfile": {
                "type": "string",
                "description": "The path to the input file containing the email message."
            },
            "outputfile": {
                "type": "string",
                "description": "The path to the output file where the extracted email will be written."
            }
        },
        "additionalProperties": False,
        "required": ["inputfile", "outputfile"],
    }
}
    },
    {
        "type": "function",
        "function":{
            "name": "generate_markdown_index",
            "description": "Generates an index file mapping markdown file names to titles.",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "The directory containing markdown files."
                    },
                    "output_file": {
                        "type": "string",
                        "description": "The path to the output file where the index will be written."
                    }
                },
                "additionalProperties": False,
                "required": ["directory", "output_file"],
            }
        }
    },
    {
        "type": "function",
        "function":{
            "name":"card_ocr",
            "description": "This function will take the input image path and output file path as input and extract the credit card number from the image",
            "parameters":{
                "type":"object",
                "properties":{
                    "inputimage":{
                        "type":"string",
                        "description":"The path to the input image"
                    },
                    "outputfile":{
                        "type":"string",
                        "description":"The path to the output file"
                    }
            },
            "additionalProperties": False,
            "required": ["inputimage","outputfile"]
            }
        }
    },
    {
        "type": "function",
        "function":{
            "name":"similar_comments",
            "description": "This function will take the input file path and output file path as input and find two similar comments in the input file and write them to the output file",
            "parameters":{
                "type":"object",
                "properties":{
                    "inputfile":{
                        "type":"string",
                        "description":"The path to the input file"
                    },
                    "outputfile":{
                        "type":"string",
                        "description":"The path to the output file"
                    }
            },
            "additionalProperties": False,
            "required": ["inputfile","outputfile"]
            }
        }
    },
    {
        "type": "function",
        "function":{
        "name":"sql_query",
        "description":"This function will take the database file path, table name, ticket type, and output file path as input and query the database to find the total sales of the ticket type and write into the output file",
        "parameters":{
            "type":"object",
            "properties":{
                "database":{
                    "type":"string",
                    "description":"The path to the database file"
                },
                "table":{
                    "type":"string",
                    "description":"The table name in the prompt"
                },
                "type":{
                    "type":"string",
                    "description":"The ticket type in the prompt"
                },
                "outputfile":{
                    "type":"string",
                    "description":"The path to the output file"
                }

        },
        "additionalProperties": False,
        "required": ["database","table","type","outputfile"]
        }
        }
    },{
        "type": "function",
        "function":{
            "name":"fetch_api",
            "description":"This function will take the input url, parameters, and save path as input and fetch the API response and write it to the save path",
            "parameters":{
                "type":"object",
                "properties":{
                    "url":{
                        "type":"string",
                        "description":"The url in the prompt"
                    },
                    "parameters":{
                        "type":"object",
                        "description":"The optional query parameters in the prompt",
                        "properties": {}
                    },
                    "save_path":{
                        "type":"string",
                        "description":"The path to the save path"
                    }
            },
            "additionalProperties": False,
            "required": ["url","save_path","parameters"]
            }
        }
    },{
        "type": "function",
        "function":{
            "name":"clone_repo",
            "description":"This function will take the input url and clone the repository from the url",
            "parameters":{
                "type":"object",
                "properties":{
                    "url":{
                        "type":"string",
                        "description":"The url in the prompt"
                    }
            },  
            "additionalProperties": False,
            "required": ["url"]
            }    
        }
    },
    {
        "type":"function",
        "function":{
            "name":"run_query",
            "description":"This function will take the input query and database file path as input and run the query on the database",
            "parameters":{
                "type":"object",
                "properties":{
                    "query":{
                        "type":"string",
                        "description":"The query in the prompt"
                    },
                    "database":{
                        "type":"string",
                        "description":"The database file path in the prompt"
                    },
                    "db_type":{
                        "type":"string",
                        "enum": ["sqlite3", "duckdb"],
                        "description":"The database type in the prompt"
                    }
            },
            "additionalProperties": False,
            "required": ["query","database","db_type"]
            }
        }
    },
    {
        "type": "function",
        "function":{
            "name":"scrape",
            "description":"This function will take the input url and file path as input and scrape the url and write the content to the file, however the filepath is optional",
            "parameters":{
                "type":"object",
                "properties":{
                    "url":{
                        "type":"string",
                        "description":"The url in the prompt"
                    },
                    "file_path":{
                        "type":"string",
                        "description":"Optional file path to save the scraped content, return an empty string if not provided"
                    }
            },              
            "additionalProperties": False,
            "required": ["url","file_path"]
            }
        }
    },
    {
        "type": "function",
        "function":{
            "name":"comp_resize_image",
            "description":"This function will take the input file path and output file path as input and compress and resize the image",
            "parameters":{
                "type":"object",
                "properties":{
                    "inputfile":{
                        "type":"string",
                        "description":"The path to the input image"
                    },
                    "outputfile":{
                        "type":"string",
                        "description":"The path to the output image"
                    }
            }, 
            "additionalProperties": False,
            "required": ["inputfile","outputfile"]
            }
        }
    },
    {
        "type": "function",
        "function":{
            "name":"transcribe_audio",
            "description":"This function will take the input mp3 file path and output file and write the transcription of the audio to the output file",
            "parameters":{
                "type":"object",
                "properties":{
                    "mp3_path":{
                        "type":"string",
                        "description":"The path to the input mp3 file"
                    },
                    "outputfile":{
                        "type":"string",
                        "description":"The path to the output file"
                    }
            },
            "additionalProperties": False,  
            "required": ["mp3_path","outputfile"]
            }
        }
    },
    {
        "type": "function",
        "function":{
            "name":"convert_md_html",
            "description":"This function will take the input markdown file path and output file path as input and convert the markdown file to html",
            "parameters":{
                "type":"object",
                "properties":{
                    "md_file":{
                        "type":"string",
                        "description":"The path to the input markdown file"
                    },
                    "html_file":{
                        "type":"string",
                        "description":"The path to the output html file"
                    }
            },
            "additionalProperties": False,
            "required": ["md_file","html_file"]
            }
        }
    }
]   