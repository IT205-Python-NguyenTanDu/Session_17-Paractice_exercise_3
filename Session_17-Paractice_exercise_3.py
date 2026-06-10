import itertools

teams_list = []
match_schedule = []


def input_teams():
    """
    Nhập và chuẩn hóa danh sách đội tuyển.

    Returns:
        None
    """
    global teams_list

    print("\n--- NHẬP DANH SÁCH ---")

    raw_input_data = input(
        "Nhập các đội (cách nhau bởi dấu phẩy): "
    )

    teams = [
        team.strip().upper()
        for team in raw_input_data.split(",")
        if team.strip()
    ]

    unique_teams = []
    seen = set()

    for team in teams:
        if team not in seen:
            unique_teams.append(team)
            seen.add(team)

    teams_list = unique_teams

    print(
        f"Đã ghi nhận {len(teams_list)} đội: {teams_list}"
    )


def generate_match_schedule():
    """
    Tạo lịch thi đấu vòng tròn một lượt.

    Returns:
        list: Danh sách trận đấu.
    """
    global match_schedule

    if len(teams_list) < 2:
        print(
            "Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu."
        )
        return []

    matches = itertools.combinations(
        teams_list,
        2
    )

    match_schedule = [
        f"{team_a} vs {team_b}"
        for team_a, team_b in matches
    ]

    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")

    for index, match in enumerate(
        match_schedule,
        start=1
    ):
        print(f"{index}. {match}")

    print(
        f"Tổng số trận đấu: {len(match_schedule)} trận."
    )

    return match_schedule


def generate_match_ids():
    """
    Sinh Match ID cho toàn bộ lịch thi đấu.

    Returns:
        None
    """
    if not match_schedule:
        print(
            "Vui lòng tạo lịch thi đấu trước khi sinh mã ID."
        )
        return

    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")

    for index, match in enumerate(
        match_schedule,
        start=1
    ):
        team_a, team_b = match.split(" vs ")

        code_a = f"{team_a[:3]:X<3}"
        code_b = f"{team_b[:3]:X<3}"

        match_id = (
            f"M{index:02d}-{code_a}-{code_b}"
        )

        print(
            f"Trận {index:<2} ({match:<20}) -> ID: {match_id}"
        )


def display_menu():
