<?php

include __DIR__ . '/Parsedown.php';

$directory = __DIR__ . '/../';
$scanned_directory = array_diff(scandir($directory), array('..', '.'));

$parser = new Parsedown;

$generated = [];

foreach ($scanned_directory as $file) {
    $ext = pathinfo($file, PATHINFO_EXTENSION);
    if ('md' !== $ext) {
        continue;
    }

    $content = file_get_contents(__DIR__ . '/../' . $file);
    $jsonFileName = str_replace('.md', '.json', $file);
    file_put_contents(__DIR__ . '/../' . $jsonFileName, $parser->json($content));

    $generated[$file] = $jsonFileName;
}

file_put_contents(__DIR__ . '/../generated_files.json', json_encode($generated));

print_r($generated);