package usi.si.seart;

import gumtree.spoon.AstComparator;
import gumtree.spoon.diff.Diff;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Main {

    private Main() {
    }

    public static void main(String[] args) throws IOException {
        if (args.length != 2) {
            throw new IllegalArgumentException("Usage: [path_before] [path_after]");
        }

        AstComparator comparator = new AstComparator(true);
        String before = Files.readString(Path.of(args[0]));
        String after = Files.readString(Path.of(args[1]));
        Diff diff = comparator.compare(before, after);
        int absChanges = diff.getRootOperations().size();
        System.out.println(absChanges);
    }
}
