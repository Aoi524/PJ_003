<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todoリスト-ゴミ箱</title>
    <!-- <link href="{{ asset('css/app.css') }}" rel="stylesheet"> -->
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body class="bg-gray-300">

    <div class="container mx-auto p-4">
        <nav class="flex justify-between">
            <h1 class="text-2xl font-bold mb-4">Todoリスト-ゴミ箱</h1>
        </nav>
        <ul class="list-disc pl-5">
            @foreach ($tasks as $task)
                <li class="flex justify-between mb-2">
                    <span class="text-gray-700">{{ $task->task_name }}</span>
                    <form action="{{ route('tasks.recover', $task->id) }}" method="POST" class="inline-block ml-2">
                        @csrf
                        @method('PUT')
                        <button type="submit" class="bg-green-300 text-white px-2 py-1 rounded">復元</button>
                    </form>
                </li>
            @endforeach
            @if(count($tasks) > 0)
                <form action="{{ route('tasks.deleteTrash') }}" method="POST" class="inline-block ml-2">
                    @csrf
                    @method('DELETE')
                    <button type="button" onclick="permanentDelete()" class="bg-red-500 text-white px-2 py-1 rounded">完全削除</button>
                </form>
            @endif
        </ul>
        @if($tasks->isEmpty())
            <p class="text-gray-500">ゴミ箱は空です。</p>
        @endif
    </div>
</body>
</html>