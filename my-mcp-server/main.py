from mcp.server.mcpserver import MCPServer

# 서버 이름 설정
mcp = MCPServer("ServerWei")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """두 숫자를 더합니다."""
    return a+b


@mcp.tool()
def get_user_status(username: str) -> str:
    """사용자의 현재 상태를 조회합니다."""
    return f"{username}님을 방해하지 마세요!"
    

if __name__ == "__main__":
    mcp.run()
