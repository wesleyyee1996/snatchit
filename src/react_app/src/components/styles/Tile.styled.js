import styled from 'styled-components';

export const StyledTile = styled.div`
  width: 7vmin;
  height: 7vmin;
  background-color: #EFD26B;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 1px;
  font-size: 3.3vmin;
  font-weight: 400;
  text-align: center;
  cursor: default;
  font-family: "Spinnaker", Arial, sans-serif;
  text-shadow: 1px 1px 1px rgb(255 255 255 / 90%), 0 -1px 1px rgb(255 255 255 / 20%);
  text-transform: uppercase;
  box-shadow: 1px 5px 5px rgb(0 0 0 / 80%), inset 3px 0 2px rgb(255 255 255 / 40%), inset 0 3px 0px rgb(255 255 255 / 50%), inset -2px -3px 0px rgb(143 128 82 / 60%);
`

export const StyledCenterTile = styled(StyledTile)`
  margin: 4% 4%;
  padding-top: 2%;
`

export const StyledPlayerTile = styled(StyledTile)`
  margin: 6% 6%;
`