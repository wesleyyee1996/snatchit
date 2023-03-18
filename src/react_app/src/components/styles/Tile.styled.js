import styled from "styled-components";

export const StyledTile = styled.div`
  width: 4.5vmin;
  height: 4.5vmin;
  background-color: #efd26b;
  // justify-content: center;
  align-items: center;
  border-radius: 6px;
  font-size: 2.7vmin;
  font-weight: 400;
  text-align: center;
  cursor: default;
  font-family: "Spinnaker", Arial, sans-serif;
  text-shadow: 1px 1px 1px rgb(255 255 255 / 90%),
    0 -1px 1px rgb(255 255 255 / 20%);
  text-transform: uppercase;
  box-shadow: 1px 5px 5px rgb(0 0 0 / 80%),
    inset 3px 0 2px rgb(255 255 255 / 40%),
    inset 0 3px 0px rgb(255 255 255 / 50%),
    inset -2px -3px 0px rgb(143 128 82 / 60%);
`;

export const StyledCenterTile = styled(StyledTile)`
  // flex-grow: 0;
  margin: 1% 1% 1% 1%;
  // padding-top: 2%;
  // border: 20px;
  position: absolute;
  top: ${(props) => props.top_pos}%;
  left: ${(props) => props.left_pos}%;
  transform: rotate(-${(props) => props.angle}deg);
`;

export const StyledPlayerTile = styled(StyledTile)`
  margin: 6% 6%;
`;
