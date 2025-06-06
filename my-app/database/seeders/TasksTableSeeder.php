<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class TasksTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $tasks = [
            [
                'task_name' => 'Trash Task',
                'due_date' => now()->addDays(5),
                'is_deleted' => true,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            // [
            //     'task_name' => 'Task 2',
            //     'due_date' => now()->addDays(10),
            //     'is_deleted' => false,
            //     'created_at' => now(),
            //     'updated_at' => now(),
            // ],
            // [
            //     'task_name' => 'Task 3',
            //     'due_date' => now()->addDays(15),
            //     'is_deleted' => false,
            //     'created_at' => now(),
            //     'updated_at' => now(),
            // ],
        ];

        foreach ($tasks as $task) {
            \App\Models\Task::create($task);
        }
    }
}
