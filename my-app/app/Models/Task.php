<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Task extends Model
{
    use HasFactory;

    protected $fillable = [
        'task_name',
        'due_date',
        'is_deleted',
    ];

    public static function getActiveTasks()
    {
        return self::where('is_deleted', false)->get();
    }

    public static function maskAsDeleted($id)
    {
        $task = self::find($id);
        $task->is_deleted = true;
        $task->save();
        return $task;
    }

    public static function getTrashTasks()
    {
        return self::where('is_deleted', true)->get();
    }

    public static function recoverTask($id)
    {
        $task = self::find($id);
        $task->is_deleted = false;
        $task->save();
        return $task;
    }

    public static function deleteTrashTaskPermanently(): int
    {
        return self::where('is_deleted', true)->delete();
    }
}
