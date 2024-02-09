valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]


def pair_document_with_format(doc_names, doc_formats):
    return filter(
        lambda element: element[1] in valid_formats,
        map(
            lambda index: (doc_names[index], doc_formats[index]),
            range(len(doc_formats)),
        ),
    )
