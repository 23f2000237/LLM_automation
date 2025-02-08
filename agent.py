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
                "secomd_target":{
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
]   