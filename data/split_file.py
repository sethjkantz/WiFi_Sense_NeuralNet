#!/usr/bin/env python3

import argparse
from pathlib import Path
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(
        description="Split a CSV into equal parts based on row count."
    )
    parser.add_argument(
        "input_csv",
        help="Path to input CSV file",
    )
    parser.add_argument(
        "--parts",
        type=int,
        default=12,
        help="Number of output files to create (default: 12)",
    )
    parser.add_argument(
        "--outdir",
        default=None,
        help="Output directory (default: <input_stem>_split_rows)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    input_path = Path(args.input_csv)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if args.parts < 1:
        raise ValueError("--parts must be at least 1")

    outdir = Path(args.outdir) if args.outdir else input_path.parent / f"{input_path.stem}_split_rows"
    outdir.mkdir(parents=True, exist_ok=True)

    print(f"Reading: {input_path}")
    df = pd.read_csv(input_path)

    total_rows = len(df)
    print(f"Total rows: {total_rows}")

    base_size = total_rows // args.parts
    remainder = total_rows % args.parts

    print(f"Base rows per file: {base_size}")
    print(f"Files with one extra row: {remainder}")

    start = 0
    written_total = 0

    for i in range(args.parts):
        chunk_size = base_size + (1 if i < remainder else 0)
        end = start + chunk_size

        chunk = df.iloc[start:end]

        out_file = outdir / f"{input_path.stem}_part_{i + 1:02d}.csv"
        chunk.to_csv(out_file, index=False)

        print(f"[{i + 1}/{args.parts}] Saved {out_file} ({len(chunk)} rows)")

        written_total += len(chunk)
        start = end

    print(f"Done. Wrote {args.parts} files to: {outdir}")
    print(f"Total rows written: {written_total}")


if __name__ == "__main__":
    main()