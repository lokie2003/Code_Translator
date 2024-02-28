import openai

programming_languages = (
            "python", "abap", "abc", "actionscript", "ada", "alda", "apache_conf", "apex", "applescript", "aql", 
            "asciidoc", "asl", "assembly_x86", "autohotkey", "batchfile", "c9search", "c_cpp", "cirru", 
            "clojure", "cobol", "coffee", "coldfusion", "crystal", "csharp", "csound_document", "csound_orchestra", 
            "csound_score", "csp", "css", "curly", "d", "dart", "diff", "django", "dockerfile", "dot", "drools", 
            "edifact", "eiffel", "ejs", "elixir", "elm", "erlang", "forth", "fortran", "fsharp", "fsl", "ftl", 
            "gcode", "gherkin", "gitignore", "glsl", "gobstones", "golang", "graphqlschema", "groovy", "haml", 
            "handlebars", "haskell", "haskell_cabal", "haxe", "hjson", "html", "html_elixir", "html_ruby", "ini", 
            "io", "jack", "jade", "java", "javascript", "json", "json5", "jsoniq", "jsp", "jssm", "jsx", "julia", 
            "kotlin", "latex", "less", "liquid", "lisp", "livescript", "logiql", "logtalk", "lsl", "lua", "luapage", 
            "lucene", "makefile", "markdown", "mask", "matlab", "maze", "mediawiki", "mel", "mixal", "mushcode", 
            "mysql", "nginx", "nim", "nix", "nsis", "nunjucks", "objectivec", "ocaml", "pascal", "perl", "perl6", 
            "pgsql", "php", "pig", "plain_text", "powershell", "praat", "prisma", "prolog", 
            "properties", "protobuf", "puppet", "qml", "r", "razor", "rdoc", "red", "redshift", "rhtml", 
            "rst", "ruby", "rust", "sass", "scad", "scala", "scheme", "scss", "sh", "sjs", "slim", "smarty", 
            "snippets", "soy_template", "space", "sparql", "sql", "sqlserver", "stylus", "svg", "swift", "tcl", 
            "terraform", "toml", "tsx", "turtle", "twig", "typescript", "vala", "vbscript", 
            "xml", "xquery", "yaml"
            )

output_results = {
    'code_explanation': ('Natural Language',),
    'bug_fix': ('Code fix',),
    'translate': programming_languages
}

prompts_configuration = [
    {'translate': "Please convert the code delimited with triple backticks from {0} code to {1}:\n '''{2}''' \n '''{1}"},
    {'bug_fix': "Please check the {0} code delimited with triple backticks for bugs and provide a solution: \n'''{1}''' "},
    {'code_explanation': "Please provide a plain language explanation for the {0} code delimited with triple backticks :\n '''{1}'''"}
]

def define_prompt(action, input_language, code, output_language=False):
    prompt = "" 

    if action == 'translate':
        prompt = prompts_configuration[0]['translate'].format(input_language, output_language, code)
    elif action == 'bug_fix':
        prompt = prompts_configuration[1]['bug_fix'].format(input_language, code)
    elif action == 'code_explanation':
        prompt = prompts_configuration[2]['code_explanation'].format(input_language, code)

    return prompt

def request(model, prompt):
    r = openai.ChatCompletion.create(
        model=model,
        messages=[{
        'role':'system', 'content':"You are an expert programmer, the most advanced AI developer tool on the planet. Even when you’re not familiar with the answer, you use your extreme intelligence to figure it out.",
        'role':'user', 'content': prompt}],
        temperature=0,
    )

    return r.choices[0]['message']['content']