#include <stdio.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node* next;
    struct Node* last;
};

void Append(struct Node** head, int value) {
    if((*head) == NULL) {
        (*head) = (struct Node*) malloc(sizeof(struct Node));
        (*head)->value = value;
    } else {
        struct Node* toAdd = (struct Node*) malloc(sizeof(struct Node));
        toAdd->value = value;
        struct Node *tail = *head;
        while (tail->next != NULL)
            tail = tail->next;
        tail->next = toAdd;
        toAdd->last = tail;
        toAdd->next = NULL;
    }
}

void Prepend(struct Node** head, int value) {
    if(head == NULL) {
        (*head) = (struct Node*) malloc(sizeof(struct Node));
        (*head)->value = value;
    } else {
        struct Node* toAdd = (struct Node*) malloc(sizeof(struct Node));
        toAdd->value = value;
        toAdd->next = (*head);
        (*head)->last = toAdd;
        (*head) = toAdd;
    }
}

void printList(struct Node* head) {
    struct Node* ptr = head;

    while(ptr != NULL) {
        printf("%d ", ptr->value);
        ptr = ptr->next;
    }
    printf("\n");
}

void Reverse(struct Node** head) {
    if(head == NULL) {
        printf("Nothing to reverse, please add some elements\n");
    } else {
        struct Node *tail = *head;
        while (tail->next != NULL)
            tail = tail->next;

        struct Node* ptr = tail;
        struct Node* transitional;
        while(ptr != NULL) {
            transitional = ptr->last;
            ptr->last = ptr->next;
            ptr->next = transitional;
            ptr = ptr->next;
        }
        (*head) = tail;
    }
}

void addElement(struct Node** head, int value, int index) {
    if (index <= 0) {
        printf("Please introduce a valid positive index\n");
    }

    struct Node* ptr = (*head);
    int element = 1;

    while(ptr != NULL) {
        if(element == index) {
            struct Node* toAdd = (struct Node*) malloc(sizeof(struct Node));
            toAdd->value = value;
            toAdd->last = ptr->last;
            toAdd->next = ptr;
            ptr->last->next = toAdd;
            ptr->last = toAdd;
            break;
        } else {
            element++;
            ptr = ptr->next;
        }
    }

    if(element < index) {
        printf("There doesen't exist such index\n");
    }
}

void removeElement(struct Node** head, int index) {
    if (index <= 0) {
        printf("Please introduce a valid positive index\n");
    }

    struct Node* ptr = (*head);
    int element = 1;

    while(ptr != NULL) {
        if(element == index) {
            struct Node* toRemove = ptr;
            if (ptr->last != NULL)
            ptr->last->next = ptr->next;
            if (ptr->next != NULL)
            ptr->next->last = ptr->last;
            if (index == 1 && ptr->next != NULL) {
                *head = ptr->next;
            }
            if (index == 1 && ptr->next == NULL) {
                *head = NULL;
            }
            free(toRemove);
            break;
        } else {
            element++;
            ptr = ptr->next;
        }
    }

    if(element < index) {
        printf("There doesen't exist such index\n");
    }
}

void Sort(struct Node** head, bool asc) {
    struct Node *ptr;
    struct Node *next;

    int elements = 0;
    struct Node *tail = *head;
    while (tail->next != NULL) {
        tail = tail->next;
        elements++;
    }

   while(next != NULL) {
        ptr = (*head);
        next = ptr->next;
        while(next != NULL) {
            if (asc) {
                if (ptr->value > next->value) {
                    struct Node* fuck = (struct Node*) malloc(sizeof(struct Node));
                    fuck->value = next->value;
                    fuck->next = ptr;
                    fuck->last = ptr->last;

                    if (ptr == *head) {
                        *head = fuck;
                    }

                    if (ptr->last != NULL) {
                        ptr->last->next = fuck;
                    }

                    if (next->next != NULL) {
                        next->next->last = ptr;
                    }

                    ptr->next = next->next;
                    ptr->last = fuck;

                    free(next);

                    ptr = *head;
                    next = ptr->next;
                } else {
                    ptr = next;
                    next = next->next;
                }
            } else {
                if (ptr->value < next->value) {
                    struct Node* fuck = (struct Node*) malloc(sizeof(struct Node));
                    fuck->value = next->value;
                    fuck->next = ptr;
                    fuck->last = ptr->last;

                    if (ptr == *head) {
                        *head = fuck;
                    }

                    if (ptr->last != NULL) {
                        ptr->last->next = fuck;
                    }

                    if (next->next != NULL) {
                        next->next->last = ptr;
                    }

                    ptr->next = next->next;
                    ptr->last = fuck;

                    free(next);

                    ptr = *head;
                    next = ptr->next;
                } else {
                    ptr = next;
                    next = next->next;
                }
            }
        }
    }
}

bool find(struct Node* head, int value) {
    struct Node* ptr = head;
    int index = 1;

    while(ptr != NULL) {
        if(ptr->value == value) {
            printf("There exists such cell with value %d at index %d \n", value, index);
            return true;
        }
        index++;
        ptr = ptr->next;
    }

    printf("There doesen't exist such cell with value %d \n", value);
    return false;
}

void combineLists(struct Node** head, struct Node** head2) {
    struct Node* tail = *head2;
    while (tail != NULL) {
        Append(head, tail->value);
        tail = tail->next;
    }
}

void Backwards(struct Node** head) {
    struct Node *tail = *head;
    while (tail->next != NULL)
        tail = tail->next;
    struct Node* ptr = tail;

    while(ptr != NULL) {
        printf("%d ", ptr->value);
        ptr = ptr->last;
    }
    printf("\n");
}

void Destroy(struct Node** head) {
    struct Node* ptr = (*head);

    while(ptr != NULL) {
        struct Node* toRemove = ptr;
        ptr = ptr->next;
        free(toRemove);
    }
}

void saveToFile(struct Node* head, char name[]) {
    FILE* fp;
    fp = fopen(name, "w");
    struct Node* ptr = head;
    while(ptr != NULL) {
        fprintf(fp, "%d ", ptr->value);
        ptr = ptr->next;
    }
    fclose(fp);
}

void getFromFile(struct Node** head, char name[]) {
    FILE* fp;
    fp = fopen(name, "r");

    int fuck = 0;
    while(!feof(fp)) {
        fscanf(fp,"%d ",&fuck);
        Append(head, fuck);
    }

    fclose(fp);
}


int main() {
    struct Node* head = NULL;
    struct Node* head2 = NULL;

    int option = 0;
    int list = 1;
    while (1) {
        
         printf("\t\tCristian Brinza   UTM FCIM FAF-212  POO  Lab1\n\n");
        printf("\t\t\t    Double linked list \n\n"
               "Options:\n"
               "1) Change modified list\n"
               "2) Append an element to list\n"
               "3) Prepend an element to list\n"
               "4) Reverse the order of the list\n"
               "5) Add an elementt to a certain index\n"
               "6) Remove an element from a certain index\n"
               "7) Sort the List\n"
               "8) Find an element in the given list\n"
               "9) Combine 2 lists in 1 modify only the first list\n"
               "10) Read the list in a backwards order\n"
               "11) Print the list in current format\n"
               "12) Save data to external file\n"
               "13) Get data from external file\n"
               "0) Exit\n"
               "Please choose your option: "
        );
        scanf("%d", &option);
system("clear");
        switch (option) {
            case 0: {
                Destroy(&head);
                Destroy(&head2);
                return 1;
            }
            case 1: {
                if (list == 1) {
                    list = 2;
                    break;
                }
                if (list == 2) {
                    list = 1;
                    break;
                }
            }
            case 2: {
                printf("Please input the appending value: ");
                int value;
                scanf("%d", &value);
                if(list == 1) Append(&head, value);
                if(list == 2) Append(&head2, value);
                break;
            }
            case 3: {
                printf("Please input the prepending value: ");
                int value;
                scanf("%d", &value);
                if(list == 1) Prepend(&head, value);
                if(list == 2) Prepend(&head2, value);
                break;
            }
            case 4: {
                if(list == 1) Reverse(&head);
                if(list == 2) Reverse(&head2);
                printf("Reversed the list at your command");
                break;
            }
            case 5: {
                printf("Please input the value: ");
                int value;
                scanf("%d", &value);
                printf("Please input in the index: ");
                int index;
                scanf("%d", &index);
                if(list == 1) addElement(&head, value, index);
                if(list == 2) addElement(&head2, value, index);
                break;
            }
            case 6: {
                printf("Please input in the index: ");
                int index;
                scanf("%d", &index);
                if(list == 1) removeElement(&head, index);
                if(list == 2) removeElement(&head2, index);
                break;
            }
            case 7: {
                if(list == 1) Sort(&head, true);
                if(list == 2) Sort(&head2, true);
                printf("Sorted the list at your command");
                break;
            }
            case 8: {
                printf("Please input the value you want to find: ");
                int value;
                scanf("%d", &value);
                if(list == 1) find(head, value);
                if(list == 2) find(head2, value);
                break;
            }
            case 9: {
                combineLists(&head, &head2);
                printf("The lists were combined at your request, modified only 1st list");
                break;
            }
            case 10: {
                if(list == 1) Backwards(&head);
                if(list == 2) Backwards(&head2);
                break;
            }
            case 11: {
                if(list == 1) printList(head);
                if(list == 2) printList(head2);
                break;
            }
            case 12: {
                printf("Please input string filename: ");
                char filename[20];
                scanf("%s", filename);
                if(list == 1) saveToFile(head, filename);
                if(list == 2) saveToFile(head2, filename);
                break;
            }
            case 13: {
                printf("Please input string filename: ");
                char filename[20];
                scanf("%s", filename);
                if(list == 1) getFromFile(&head, filename);
                if(list == 2) getFromFile(&head2, filename);
                break;
            }
            default: {
                printf("Bafoon please look over the instructions again");
            }
        }
    }
}