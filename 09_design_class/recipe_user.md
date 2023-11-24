# Follow the design recipe to implement the following user story in your project:

## 1. Describe the Problem
> As a user
> So that I can record my experiences
> I want to keep a regular diary

> As a user
> So that I can reflect on my experiences
> I want to read my past diary entries

>  As a user
>  So that I can reflect on my experiences in my busy day
>  I want to select diary entries to read based on how much time I have and my reading speed

> As a user
> So that I can keep track of my tasks
> I want to keep a todo list along with my diary

> As a user
> So that I can keep track of my contacts
> I want to see a list of all of the mobile phone numbers in all my diary entries


## 2. Design the Class Interface

#_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

#Verbs
record experiences
keep
reflect/read past diary entries
select
keep track of tasks
see a list
add
mark complete
list incomplete
list complete




#Nouns

experiences
diary
diary entries
time
reading szpeed
todolist
tasks
phone nos


# EXAMPLE
```python
class Diary:
    def __init__(self):
        pass
    
    def add(self, entry):
        pass

    def all(self):
        pass
        

class Diary_entry:
    def __init__(self, title, contents):
        pass

    
class TaskList:
    def add(self, tasks):
        adds tasks
        pass

    def incomplete():
        returns lists of incomplete taks
        pass

    def complete():
        returns lists of complete task
        pass

class Task:
    def __init__(self, todo):
        pas

    def mark_complete(self):
        # returns nothing
        # marks the task complete
        pass

class Phonenumbers:
    def __init__(self, diary):
        # an instance of diary
        pass

    def extract():
        #returns a list of strings representing
        # a list of phone number
        pass

class ReadableEntryFinder():
       def __init__(self, wpm, min):
        # returns the longest diary entry that can be read in the given wpm and min
        pass

        def extract():
        #returns a list of strings representing
        # a list of phone number
        pass

```


## 3. Create Examples as Integration Tests

"""
Intially, diary has no entries
"""

# diary = Diary()
# entry1 = Diary_entry("Title 1" , "Contents 1")
# entry2 = Diary_entry("Title 2" , "Contents 2")
# diary.add(entry1)
# diary.add(entry2)
# assert diary.all() == [entry1, entry2]


"""
When multiple tasks are added
They are all added to the list of tasks
"""

# tracker = TaskTracker()
# tracker.add("Go Running")
# tracker.add("Walk the dog")
# tracker.add("Task out the trash")
# tracker.incomplete() = ["Go Running", "Walk the dog", "Task out the trash"]

"""
When multiple tasks are added
And mark 1 as complete
They are all added to the incomplete list of tasks
"""

# tracker = TaskTracker()
# task1 = Task("Go Running")
# task2 = Task("Walk the dog")
# task3 = Task("Task out the trash")
# tracker.add task1
# tracker.add task2
# tracker.add task3
# task2.mark_complete()
# tracker.incomplete() = [task1, task3]

"""
When multiple tasks are added
And mark 1 as complete
They are all added to the list of tasks
"""

# tracker = TaskTracker()
# task1 = Task("Go Running")
# task2 = Task("Walk the dog")
# task3 = Task("Task out the trash")
# tracker.add task1
# tracker.add task2
# tracker.add task3
# task2.mark_complete()
# tracker.complete() = [task2 ]


"""
When I add multiple diary entries
And i call Phonenosextract
i get list of phone nos from all diary entries
"""

# diary = Diary()
# entry1 = Diary_entry("Title 1" , "My friend   0700000000 and  0700000001")
# entry2 = Diary_entry("Title 2" , "My Contents 0700000002")
# diary.add(entry1)
# diary.add(entry2)
# extraxtor = Phonenumberextractor(diary)
# extractor.extract() == [07000000000, 0700000001, 0700000002]


"""
When I add no diary entries, 
And I call Phone NosExtractor
It returns None
"""

# diary = Diary()
# extractor = PhoneNumberyExtractor(diary)
# extractor.extract() == []

"""
When I one multiple entries
And I call readble EntryExtractor"extract
With wpm of 2 and min of 2 
It gets that diary entry
"""

# diary = Diary()
# entry1 = Diary_entry("Title 1" , "One Two Three Four")
# diary.add(entry1)
# extractor = ReadbleEntryExtractor(diary)
# extractor.extract(wpm = 2, min =2) == [entry1 ]

"""
When I add multiple entries, one readble
And I call readble EntryExtractor"extract
With wpm of 2 and min of 2 
It gets the readble diary entry
"""

# diary = Diary()
# entry1 = Diary_entry("Title 1" , "One Two Three Four Five")
# entry2 = Diary_entry("Title 2" , "One Two Three Four")
# diary.add(entry1)
# diary.add(entry2)
# extractor = ReadbleEntryExtractor(diary)
# extractor.extract(wpm = 2, min =2) == [entry2 ]


"""
When I add multiple entries, one readble
And I call readble EntryExtractor"extract
With wpm of 2 and min of 2 
It gets the longest readble diary entry
"""

# diary = Diary()
# entry1 = Diary_entry("Title 1" , "One Two Three Four Five")
# entry2 = Diary_entry("Title 2" , "One Two Three")
# entry2 = Diary_entry("Title 2" , "One Two Three Four")
# diary.add(entry1)
# diary.add(entry2)
# diary.add(entry3)
# extractor = ReadbleEntryExtractor(diary)
# extractor.extract(wpm = 2, min =2) == [entry3 ]


"""
When I add no diary entries, 
And I call Readable EntryExtractor
It returns None
"""

# diary = Diary()
# extractor = ReadbleEntryExtractor(diary)
# extractor.extract(wpm = 2, min =2) == [entry3 ]



## 4. Create Examples as Unit Tests


# Diary

# def test_for_adding_in_diary():
    diary = Diary()
    assert diary.all() == []

# DiaryEntry

# def test_for_adding_in_diaryentry():
entry = DiaryEntry("Title 1" , "Contents 1")
entry.title = "Title 1"
entry.contents = "Contents 1"

# TaskList

task_list = TaskList()
task_list.all() == []

# Task

"""
When constructs with a title
"""

task = Task("Walk the dog")
task.todo == "Walk the dog"



4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

