interface Props {
    children: string;
    color?: "primary" | "secondary" | "success" | "danger" | "warning";
    onClick: () => void;
}

const Button = ({children, color = "primary", onClick}: Props) => {
  return (
    <button type="button" className={"btn btn-" + color + " btn-lg"} onClick={onClick}>{children}</button>
    )
}

export default Button