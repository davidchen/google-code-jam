TEST_FILE = 'C-small-practice-2.in'


def main():
    f = open(TEST_FILE, 'r')
    s = open('bs-output-small.txt', 'w')
    num_test_cases = int(f.readline())

    for test_case in range(1, num_test_cases + 1):
        numbers = f.readline().split()
        print(numbers)
        stalls = int(numbers[0])
        people = int(numbers[1])

        result = solve(stalls, people)
        max = result[0]
        min = result[1]

        # print('Case #{}: {} {}\n'.format(test_case, max, min))
        s.write('Case #{}: {} {}\n'.format(test_case, max, min))

        # exit()

    f.close()
    s.close()


def solve(s, p):
    list_of_empty_stall_segments = []
    list_of_stall_segments_sizes = []

    list_of_empty_stall_segments.append([1, s])
    list_of_stall_segments_sizes.append(s - 1 + 1)

    for person_num in range(1, p + 1):

        print('\n\nPERSON #{} -----------------'.format(person_num))
        print('EMPTY STALL SEGMENTS:', list_of_empty_stall_segments)
        print('EMPTY STALL SEGMENT SIZES:', list_of_stall_segments_sizes)

        # first find the segment of largest size and the middle stall of this segment
        size_of_max_segment = max(list_of_stall_segments_sizes)
        index_of_max_segment = list_of_stall_segments_sizes.index(size_of_max_segment)
        segment_in_question = list_of_empty_stall_segments[index_of_max_segment]
        segment_start_stall = segment_in_question[0]
        segment_end_stall = segment_in_question[1]

        if size_of_max_segment % 2 == 0:  # if there are an even number of stalls:
            midpoint_stall = (segment_start_stall + segment_end_stall - 1) // 2
        else:
            midpoint_stall = (segment_start_stall + segment_end_stall) // 2

        new_left_segment = [segment_start_stall, midpoint_stall - 1]
        new_left_segment_size = (midpoint_stall - 1) - segment_start_stall + 1
        new_right_segment = [midpoint_stall + 1, segment_end_stall]
        new_right_segment_size = (segment_end_stall) - (midpoint_stall + 1) + 1

        # remove the original max segment used
        del list_of_empty_stall_segments[index_of_max_segment]
        del list_of_stall_segments_sizes[index_of_max_segment]

        # add the two new "halved" segments
        list_of_empty_stall_segments.append(new_left_segment)
        list_of_stall_segments_sizes.append(new_left_segment_size)
        list_of_empty_stall_segments.append(new_right_segment)
        list_of_stall_segments_sizes.append(new_right_segment_size)

        print('SIZE OF MAX SEGMENT:', size_of_max_segment, '\tINDEX:', index_of_max_segment)
        print('SEGMENT:', segment_in_question)
        print('MIDPOINT:', midpoint_stall)
        print('NEW LEFT SEGMENT:', new_left_segment, '\tNEW RIGHT SEGMENT:', new_right_segment)

    empty_stalls_to_the_left = new_left_segment[1] - new_left_segment[0] + 1
    empty_stalls_to_the_right = new_right_segment[1] - new_right_segment[0] + 1

    max_stalls = max(empty_stalls_to_the_left, empty_stalls_to_the_right)
    min_stalls = min(empty_stalls_to_the_left, empty_stalls_to_the_right)

    return (max_stalls, min_stalls)


if __name__ == '__main__':
    main()
