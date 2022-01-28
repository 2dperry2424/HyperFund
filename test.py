from datetime import timedelta, date

membership_cost = 50
membership_count = 18
memberships_at_work = membership_cost * membership_count
reward_bank = 0

claimed_money_off_table = 0

memberships = {}
# initialize starting membership count
for each in range(membership_count):
    memberships[each + 1] = {"paid_out": 0, "still_paying": True}


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2022, 1, 1)
end_date = date(2025, 1, 1)


for day in daterange(start_date, end_date):

    daily_reward = 0

    for membership in memberships.keys():
        if memberships[membership]["still_paying"] == True:
            daily_reward += 0.005 * membership_cost
            memberships[membership]["paid_out"] += 0.005 * membership_cost

        if memberships[membership]["paid_out"] >= membership_cost * 3:
            memberships[membership]["still_paying"] = False

    reward_bank += daily_reward * 0.5
    claimed_money_off_table += daily_reward * 0.5

    if reward_bank >= membership_cost:
        membership_count += 1
        memberships[membership_count] = {}
        memberships[membership_count]["paid_out"] = 0
        memberships[membership_count]["still_paying"] = True
        reward_bank -= membership_cost

    print(
        f"{day}  ||  reward_bank:  {reward_bank}  ||  memberships_still_active : {[x for x in memberships if memberships[x]['still_paying'] == True]}  ||  claimed $: {claimed_money_off_table}"
    )
    # print(
    #     f"{day}  ||  reward_bank:  {reward_bank}  ||  memberships : { memberships }  ||  claimed $: {claimed_money_off_table}"
    # )
