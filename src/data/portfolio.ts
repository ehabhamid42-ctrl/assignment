export type Skill = {
  id: string;
  name: string;
  detail: string;
};

export type EducationItem = {
  id: string;
  period: string;
  title: string;
  detail: string;
};

export type Project = {
  id: string;
  title: string;
  problem: string;
  contribution: string;
  technology: string;
  year: string;
};

export const skills: Skill[] = [
  {
    id: 'python',
    name: 'Python programming',
    detail: 'Readable scripts and programs for automation, data handling, and small command-line tools.',
  },
  {
    id: 'java',
    name: 'Java programming',
    detail: 'Object-oriented programs with classes, collections, and clear separation between logic and input.',
  },
  {
    id: 'c',
    name: 'C programming',
    detail: 'Low-level programs that manage memory and pointers directly for speed and control.',
  },
  {
    id: 'cpp',
    name: 'C++ programming',
    detail: 'Structured and object-oriented programs that combine the control of C with reusable classes.',
  },
];

export const education: EducationItem[] = [
  {
    id: 'ines',
    period: 'September 2024 onward',
    title: 'INES-Ruhengeri',
    detail: 'Software Engineering. Registration number 25/27950.',
  },
];

export const projects: Project[] = [
  {
    id: 'python-automation',
    title: 'Python automation tool',
    year: '2026 · Python',
    problem:
      'Repeated manual work needed a small tool that could run the same steps and report a clear result each time.',
    contribution:
      'I wrote the Python program, broke the task into functions, and handled bad input with clear messages instead of crashing.',
    technology: 'Python',
  },
  {
    id: 'java-console-app',
    title: 'Java console application',
    year: '2026 · Java',
    problem:
      'A small record-keeping task needed classes that could store, list, and search entries from a menu.',
    contribution:
      'I designed the Java classes, wired the menu to the logic, and kept input handling separate from the data model.',
    technology: 'Java',
  },
  {
    id: 'c-file-parser',
    title: 'C file parser',
    year: '2026 · C',
    problem:
      'A text file needed to be read, checked, and summarised quickly without a heavy runtime.',
    contribution:
      'I wrote the C program, managed buffers and pointers carefully, and freed every allocation before exit.',
    technology: 'C',
  },
  {
    id: 'cpp-inventory',
    title: 'C++ inventory program',
    year: '2026 · C++',
    problem:
      'A simple inventory needed reusable objects that could add, remove, and total stock items.',
    contribution:
      'I built the C++ classes for items and inventory, used the standard library containers, and kept the code modular.',
    technology: 'C++',
  },
];

export const contactLinks = [
  { label: 'Email ehabhamid42@gmail.com', url: 'mailto:ehabhamid42@gmail.com' },
] as const;
