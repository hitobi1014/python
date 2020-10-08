package day10;

public class Block {
	public int kind = 7;
	public int status = 1;
	public int i = 1;
	public int j = 5;
	
	public Block() {
		init();
	}
	
	public Block(int kind) {
		this.kind = kind;
	}
	
	public void init() {
		kind = (int)(Math.random()*7+1);
		status = 1;
		i = 1;
		j = 5;
	}
	
	@Override
	public String toString() {
		return "Block [kind=" + kind + ", status=" + status + ", i=" + i + ", j=" + j + "]";
	}
	
}
