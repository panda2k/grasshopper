/** @jsxImportSource @emotion/react */


import { Fragment, useContext } from "react"
import { EventLoopContext } from "/utils/context"
import { Event, getBackendURL, isTrue } from "/utils/state"
import { BarChartIcon as LucideBarChartIcon, CalendarClockIcon as LucideCalendarClockIcon, CircleUserIcon as LucideCircleUserIcon, HomeIcon as LucideHomeIcon, ScanEyeIcon as LucideScanEyeIcon, WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { Box as RadixThemesBox, Container as RadixThemesContainer, Dialog as RadixThemesDialog, Flex as RadixThemesFlex, Link as RadixThemesLink, Separator as RadixThemesSeparator, Text as RadixThemesText } from "@radix-ui/themes"
import env from "/env.json"
import NextLink from "next/link"
import NextHead from "next/head"



const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Fragment_6499b51736be44284c15de43340cb16c () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue(connectErrors.length >= 2) ? (
  <Fragment>
  <RadixThemesDialog.Root css={{"zIndex": 9999}} open={connectErrors.length >= 2}>
  <RadixThemesDialog.Content>
  <RadixThemesDialog.Title>
  {`Connection Error`}
</RadixThemesDialog.Title>
  <RadixThemesText as={`p`}>
  {`Cannot connect to server: `}
  {(connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''}
  {`. Check if server is reachable at `}
  {getBackendURL(env.EVENT).href}
</RadixThemesText>
</RadixThemesDialog.Content>
</RadixThemesDialog.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Fragment_cb5edf864ed730e6ef1545318d0da5a2 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue(connectErrors.length > 0) ? (
  <Fragment>
  <LucideWifiOffIcon css={{"color": "crimson", "zIndex": 9999, "position": "fixed", "bottom": "30px", "right": "30px", "animation": `${pulse} 1s infinite`}} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment>
  <div css={{"position": "fixed", "width": "100vw", "height": "0"}}>
  <Fragment_cb5edf864ed730e6ef1545318d0da5a2/>
</div>
  <Fragment_6499b51736be44284c15de43340cb16c/>
</Fragment>
  <RadixThemesBox css={{"paddingBottom": "4em", "padding": "1em"}}>
  <RadixThemesFlex align={`center`} css={{"flexWrap": "wrap", "fontSize": "2em"}} gap={`2`}>
  <img css={{"width": "3em", "padding": "15px"}} src={`/profilepic.png`}/>
  <RadixThemesFlex align={`start`} direction={`column`} gap={`2`}>
  <RadixThemesBox>
  <RadixThemesText as={`p`} size={`6`}>
  {`username`}
</RadixThemesText>
</RadixThemesBox>
  <RadixThemesBox>
  <RadixThemesText as={`p`} size={`2`}>
  {`5 friends • 3 events`}
</RadixThemesText>
</RadixThemesBox>
</RadixThemesFlex>
  <RadixThemesSeparator size={`4`}/>
  <RadixThemesContainer css={{"align": "center", "justify": "center"}}>
  <RadixThemesFlex css={{"background": "#f1f1f1", "width": "100%", "height": "300px", "display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  <RadixThemesFlex css={{"display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  <img css={{"width": "5em"}} src={`/profile-blocks.png`}/>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesContainer>
  <RadixThemesSeparator size={`4`}/>
  <RadixThemesContainer>
  <RadixThemesFlex align={`center`} css={{"padding": "15px", "display": "flex", "alignItems": "center", "justifyContent": "center"}} gap={`7`}>
  <RadixThemesText as={`p`} size={`4`}>
  {`saved`}
</RadixThemesText>
  <RadixThemesText as={`p`} size={`4`}>
  {`attended`}
</RadixThemesText>
  <RadixThemesText as={`p`} size={`4`}>
  {`host`}
</RadixThemesText>
</RadixThemesFlex>
  <RadixThemesBox>
  <RadixThemesText as={`p`} size={`3`}>
  {`add cards similar to home screen`}
</RadixThemesText>
</RadixThemesBox>
</RadixThemesContainer>
</RadixThemesFlex>
  <RadixThemesBox css={{"padding": "1em", "backgroundColor": "#121212", "color": "white", "position": "fixed", "bottom": "0", "left": "0", "width": "100%"}}>
  <RadixThemesFlex align={`center`} css={{"justifyContent": "space-evenly"}} justify={`center`} gap={`3`}>
  <RadixThemesLink asChild={true} css={{"color": "white"}}>
  <NextLink href={`/`} passHref={true}>
  <LucideHomeIcon css={{"color": "var(--current-color)"}}/>
</NextLink>
</RadixThemesLink>
  <RadixThemesLink asChild={true} css={{"color": "white"}}>
  <NextLink href={`/itinerary`} passHref={true}>
  <LucideCalendarClockIcon css={{"color": "var(--current-color)"}}/>
</NextLink>
</RadixThemesLink>
  <RadixThemesLink asChild={true} css={{"color": "white"}}>
  <NextLink href={`/scan`} passHref={true}>
  <LucideScanEyeIcon css={{"color": "var(--current-color)"}}/>
</NextLink>
</RadixThemesLink>
  <RadixThemesLink>
  <LucideBarChartIcon css={{"color": "white", "href": "/leaderboard"}}/>
</RadixThemesLink>
  <RadixThemesLink asChild={true} css={{"color": "white"}}>
  <NextLink href={`/profile`} passHref={true}>
  <LucideCircleUserIcon css={{"color": "var(--current-color)"}}/>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesBox>
  <NextHead>
  <title>
  {`Profile`}
</title>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
