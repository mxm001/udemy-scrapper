import threading


def threader(courses):
    """
    Create threads to process multiple requests.
    :param courses:
    :return:
    """
    size = int((len(courses) / 10) + 1)
    thread_links = list(chunks(courses, size))
    threads = []
    flag = 0
    for x in range(0, 9):
        th = threading.Thread(target=courses, args=(thread_links[x],))
        th.start()
        threads.append(th)
        flag += 1

    for x in threads:
        x.join()


def chunks(li, size):
    """
    Yield successive n-sized chunks from l
    :param li: (list) list to chunk
    :param size: (int) size of the chunks
    :return: chunks (list) list of chunks
    """
    return [list[i:i+size] for i in range(0, len(li), size)]
