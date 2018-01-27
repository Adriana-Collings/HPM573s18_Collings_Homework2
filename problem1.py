# HUI3 Single-Attribute Utility Functions

HUI3dict = {'vision':        [1, 0.98, 0.89, 0.84, 0.75, 0.61],
            'hearing':       [1, 0.95, 0.89, 0.8, 0.74, 0.61],
            'speech':        [1, 0.94, 0.89, 0.81, 0.68],
            'ambulation':    [1, 0.94, 0.89, 0.81, 0.68],
            'dexterity':     [1, 0.95, 0.88, 0.76, 0.65, 0.56],
            'emotion':       [1, 0.95, 0.85, 0.64, 0.46],
            'cognition':     [1, 0.92, 0.95, 0.83, 0.6, 0.42],
            'pain':          [1, 0.96, 0.9, 0.77, 0.55]
            }


def get_hui3(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    """

    :param vision: level of vision
    :param hearing: level of hearing
    :param speech: level of speech
    :param ambulation: level of ambulation
    :param dexterity: level of dexterity
    :param emotion: level of emotion
    :param cognition: level of cognition
    :param pain: level of pain
    :return: HUI3 comprehensive health score
    """

    # ensure entered dimensions are acceptable values
    if not(vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Vision can only take value of 1, 2, 3, 4, 5, or 6')
    if not(hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Hearing can only take value of 1, 2, 3, 4, 5, or 6')
    if not(speech in [1, 2, 3, 4, 5]):
        raise ValueError('Speech can only take value of 1, 2, 3, 4, or 5')
    if not(ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Ambulation can only take value of 1, 2, 3, 4, 5, or 6')
    if not(dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Dexterity can only take value of 1, 2, 3, 4, 5, or 6')
    if not(emotion in [1, 2, 3, 4, 5]):
        raise ValueError('Emotion can only take value of 1, 2, 3, 4, or 5')
    if not(cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Cognition can only take value of 1, 2, 3, 4, 5, or 6')
    if not(pain in [1, 2, 3, 4, 5]):
        raise ValueError('Pain can only take value of 1, 2, 3, 4, or 5')

    hui3 = 1.371  # set hui3 to 1.371 to begin

    # function
    hui3 *= HUI3dict['vision'][vision-1]
    hui3 *= HUI3dict['hearing'][hearing - 1]
    hui3 *= HUI3dict['speech'][speech - 1]
    hui3 *= HUI3dict['ambulation'][ambulation - 1]
    hui3 *= HUI3dict['dexterity'][dexterity - 1]
    hui3 *= HUI3dict['emotion'][emotion - 1]
    hui3 *= HUI3dict['cognition'][cognition - 1]
    hui3 *= HUI3dict['pain'][pain - 1]

    hui3 -= 0.371

    return hui3


print(get_hui3(2, 1, 1, 2, 1, 2, 1, 3))
