teams_list = []
match_schedule = []


def input_teams():
    """
    Input and normalize team names.

    Parameters:
        None

    Returns:
        list: List of unique team names.
    """
    global teams_list

    print("\n--- NHẬP DANH SÁCH ---")

    while True:
        team_input = input(
            "Nhập các đội (cách nhau bởi dấu phẩy): "
        ).strip()

        if team_input == "":
            print("Lỗi: Không được để trống danh sách đội.")
            continue

        raw_teams = team_input.split(",")

        normalized_teams = [
            team.strip().upper()
            for team in raw_teams
            if team.strip() != ""
        ]

        if len(normalized_teams) == 0:
            print("Lỗi: Không có đội hợp lệ.")
            continue

        unique_teams = []

        for team_name in normalized_teams:
            if team_name not in unique_teams:
                unique_teams.append(team_name)

        teams_list = unique_teams

        print(
            f"Đã ghi nhận {len(teams_list)} đội: {teams_list}"
        )

        return teams_list


def generate_schedule():
    """
    Generate round-robin match schedule.

    Parameters:
        None

    Returns:
        list: List of matches in format 'TEAM A vs TEAM B'.
    """
    global match_schedule

    if len(teams_list) < 2:
        print(
            "Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu."
        )
        return []

    match_schedule = []

    first_index = 0

    while first_index < len(teams_list) - 1:

        second_index = first_index + 1

        while second_index < len(teams_list):

            match_text = (
                f"{teams_list[first_index]} vs "
                f"{teams_list[second_index]}"
            )

            match_schedule.append(match_text)

            second_index += 1

        first_index += 1

    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")

    for index, match_text in enumerate(
            match_schedule,
            start=1
    ):
        print(f"{index}. {match_text}")

    print(
        f"Tổng số trận đấu: {len(match_schedule)} trận."
    )

    return match_schedule


def generate_match_ids():
    """
    Generate match IDs from schedule.

    Parameters:
        None

    Returns:
        list: List of generated match IDs.
    """
    if len(match_schedule) == 0:
        print(
            "Vui lòng tạo lịch thi đấu trước khi sinh mã ID."
        )
        return []

    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")

    match_ids = []

    for match_number, match_text in enumerate(
            match_schedule,
            start=1
    ):
        teams = match_text.split(" vs ")

        team_a = teams[0]
        team_b = teams[1]

        team_a_code = f"{team_a[0:3]:X<3}"
        team_b_code = f"{team_b[0:3]:X<3}"

        match_id = (
            f"M{match_number:02d}-"
            f"{team_a_code}-"
            f"{team_b_code}"
        )

        match_ids.append(match_id)

        print(
            f"Trận {match_number} "
            f"({match_text}) -> ID: {match_id}"
        )

    return match_ids


def display_menu():
    """
    Display application menu.

    Parameters:
        None

    Returns:
        None
    """
    print(
        "\n============= ESPORTS MATCHMAKER ============="
    )
    print("1. Nhập danh sách Đội tuyển")
    print("2. Tạo lịch thi đấu")
    print("3. Tạo mã trận đấu tự động")
    print("4. Đóng hệ thống")
    print(
        "=============================================="
    )


while True:

    display_menu()

    choice = input(
        "Chọn chức năng (1-4): "
    ).strip()

    if choice == "1":
        input_teams()

    elif choice == "2":
        generate_schedule()

    elif choice == "3":
        generate_match_ids()

    elif choice == "4":
        print("Đóng hệ thống thành công.")
        break

    else:
        print(
            "Lựa chọn không hợp lệ. "
            "Vui lòng nhập từ 1 đến 4."
        )