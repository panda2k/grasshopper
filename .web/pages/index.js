/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event, getBackendURL, getRefValue, getRefValues, isTrue } from "/utils/state"
import { BarChartIcon as LucideBarChartIcon, CalendarClockIcon as LucideCalendarClockIcon, CirclePlusIcon as LucideCirclePlusIcon, CircleUserIcon as LucideCircleUserIcon, CircleXIcon as LucideCircleXIcon, HomeIcon as LucideHomeIcon, WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { Box as RadixThemesBox, Button as RadixThemesButton, Dialog as RadixThemesDialog, Flex as RadixThemesFlex, Heading as RadixThemesHeading, Link as RadixThemesLink, ScrollArea as RadixThemesScrollArea, Select as RadixThemesSelect, Text as RadixThemesText, TextField as RadixThemesTextField, Theme as RadixThemesTheme } from "@radix-ui/themes"
import env from "/env.json"
import NextLink from "next/link"
import { Drawer as VaulDrawer } from "vaul"
import "@radix-ui/themes/styles.css"
import theme from "/utils/theme.js"
import { Root as RadixFormRoot } from "@radix-ui/react-form"
import NextHead from "next/head"



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

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Fragment_e4189cc831f29355b3c1176b62dd13e8 () {
  const state__global_state = useContext(StateContexts.state__global_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  
    const handleSubmit_9ff2fe2f1c888cbe5f72b547479f8311 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{}}

        addEvents([Event("state.global_state.create_event", {form_data:form_data})])

        if (true) {
            $form.reset()
        }
    })
    

  return (
    <Fragment>
  {isTrue(state__global_state.token_is_valid) ? (
  <Fragment>
  <VaulDrawer.Root direction={`bottom`}>
  <VaulDrawer.Trigger asChild={true}>
  <RadixThemesButton color={`lime`}>
  <LucideCirclePlusIcon css={{"color": "var(--current-color)"}}/>
</RadixThemesButton>
</VaulDrawer.Trigger>
  <VaulDrawer.Overlay css={{"position": "fixed", "left": "0", "right": "0", "bottom": "0", "top": "0", "z_index": 50, "background": "rgba(0, 0, 0, 0.5)", "zIndex": "5"}}/>
  <VaulDrawer.Portal>
  <RadixThemesTheme css={{...theme.styles.global[':root'], ...theme.styles.global.body}}>
  <VaulDrawer.Content css={{"left": "0", "right": "0", "bottom": "0", "top": "0", "position": "fixed", "z_index": 50, "display": "flex", "height": "90%", "padding": "2em", "backgroundColor": "#FFF"}}>
  <RadixThemesFlex align={`start`} css={{"width": "100%"}} direction={`column`} gap={`2`}>
  <RadixThemesFlex css={{"width": "100%"}} justify={`between`}>
  <RadixThemesHeading>
  {`Create Event`}
</RadixThemesHeading>
  <VaulDrawer.Close asChild={true}>
  <RadixThemesButton color={`lime`}>
  <LucideCircleXIcon css={{"color": "var(--current-color)"}}/>
</RadixThemesButton>
</VaulDrawer.Close>
</RadixThemesFlex>
  <RadixFormRoot className={`Root`} onSubmit={handleSubmit_9ff2fe2f1c888cbe5f72b547479f8311}>
  <RadixThemesFlex align={`start`} direction={`column`} gap={`2`}>
  <RadixThemesTextField.Input name={`title`} placeholder={`Title`} required={true}/>
  <RadixThemesTextField.Input name={`description`} placeholder={`Description`} required={true}/>
  <RadixThemesSelect.Root name={`school`} required={true}>
  <RadixThemesSelect.Trigger placeholder={`School`}/>
  <RadixThemesSelect.Content>
  <RadixThemesSelect.Group>
  {``}
  {state__global_state.school_names.map((item, index_efe375a01b46a1f2c495265a3b440b7a) => (
  <RadixThemesSelect.Item key={index_efe375a01b46a1f2c495265a3b440b7a} value={item}>
  {item}
</RadixThemesSelect.Item>
))}
</RadixThemesSelect.Group>
</RadixThemesSelect.Content>
</RadixThemesSelect.Root>
  <RadixThemesTextField.Input name={`location`} placeholder={`Location`} required={true}/>
  <RadixThemesTextField.Input min={`2024-04-20TApr:09`} name={`time`} type={`datetime-local`}/>
  <RadixThemesButton type={`submit`}>
  {`Create`}
</RadixThemesButton>
</RadixThemesFlex>
</RadixFormRoot>
</RadixThemesFlex>
</VaulDrawer.Content>
</RadixThemesTheme>
</VaulDrawer.Portal>
</VaulDrawer.Root>
</Fragment>
) : (
  <Fragment>
  <RadixThemesFlex/>
</Fragment>
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
  <RadixThemesFlex css={{"padding": "1em", "display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  <RadixThemesFlex align={`center`} css={{"fontSize": "2em"}} direction={`column`} gap={`2`}>
  <RadixThemesHeading size={`6`}>
  {`Events`}
</RadixThemesHeading>
  <RadixThemesBox css={{"width": "100%", "padding": "14px", "margin": "10px", "border-bottom": "1px solid #e0e0e0"}}>
  <RadixThemesBox css={{"asChild": true}}>
  <img css={{"height": "70%", "width": "100%", "object-fit": "cover", "object-position": "center", "border-radius": "10px", "margin-bottom": "14px"}} src={`https://acmucsd.s3.us-west-1.amazonaws.com/portal/events/46f1a42e-41e5-4103-8052-74d3e13d6a62.png`}/>
  <RadixThemesFlex>
  <RadixThemesBox css={{"margin-bottom": "10px", "spacing": "1", "height": "100%"}}>
  <RadixThemesHeading as={`h1`} size={`5`} trim={`normal`}>
  {`ACM Kickoff`}
</RadixThemesHeading>
  <RadixThemesText as={`p`} size={`4`} trim={`normal`} weight={`medium`}>
  {`ACM @ UCSD`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"margin-bottom": "10px"}} size={`3`} trim={`normal`} weight={`light`}>
  {`UC San Diego`}
</RadixThemesText>
  <RadixThemesScrollArea>
  <RadixThemesFlex css={{"height": 55, "type": "always", "scrollbars": "vertical"}}>
  <RadixThemesText as={`p`} size={`2`} trim={`both`}>
  {`Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesScrollArea>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesBox>
  <RadixThemesBox css={{"width": "100%", "padding": "14px", "margin": "10px", "border-bottom": "1px solid #e0e0e0"}}>
  <RadixThemesBox css={{"asChild": true}}>
  <img css={{"height": "70%", "width": "100%", "object-fit": "cover", "object-position": "center", "border-radius": "10px", "margin-bottom": "14px"}} src={`https://acmucsd.s3.us-west-1.amazonaws.com/portal/events/46f1a42e-41e5-4103-8052-74d3e13d6a62.png`}/>
  <RadixThemesFlex>
  <RadixThemesBox css={{"margin-bottom": "10px", "spacing": "1", "height": "100%"}}>
  <RadixThemesHeading as={`h1`} size={`5`} trim={`normal`}>
  {`ACM Kickoff`}
</RadixThemesHeading>
  <RadixThemesText as={`p`} size={`4`} trim={`normal`} weight={`medium`}>
  {`ACM @ UCSD`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"margin-bottom": "10px"}} size={`3`} trim={`normal`} weight={`light`}>
  {`UC San Diego`}
</RadixThemesText>
  <RadixThemesScrollArea>
  <RadixThemesFlex css={{"height": 55, "type": "always", "scrollbars": "vertical"}}>
  <RadixThemesText as={`p`} size={`2`} trim={`both`}>
  {`Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesScrollArea>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesBox>
  <RadixThemesBox css={{"width": "100%", "padding": "14px", "margin": "10px", "border-bottom": "1px solid #e0e0e0"}}>
  <RadixThemesBox css={{"asChild": true}}>
  <img css={{"height": "70%", "width": "100%", "object-fit": "cover", "object-position": "center", "border-radius": "10px", "margin-bottom": "14px"}} src={`https://acmucsd.s3.us-west-1.amazonaws.com/portal/events/46f1a42e-41e5-4103-8052-74d3e13d6a62.png`}/>
  <RadixThemesFlex>
  <RadixThemesBox css={{"margin-bottom": "10px", "spacing": "1", "height": "100%"}}>
  <RadixThemesHeading as={`h1`} size={`5`} trim={`normal`}>
  {`ACM Kickoff`}
</RadixThemesHeading>
  <RadixThemesText as={`p`} size={`4`} trim={`normal`} weight={`medium`}>
  {`ACM @ UCSD`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"margin-bottom": "10px"}} size={`3`} trim={`normal`} weight={`light`}>
  {`UC San Diego`}
</RadixThemesText>
  <RadixThemesScrollArea>
  <RadixThemesFlex css={{"height": 55, "type": "always", "scrollbars": "vertical"}}>
  <RadixThemesText as={`p`} size={`2`} trim={`both`}>
  {`Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesScrollArea>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesBox>
  <RadixThemesBox css={{"width": "100%", "padding": "14px", "margin": "10px", "border-bottom": "1px solid #e0e0e0"}}>
  <RadixThemesBox css={{"asChild": true}}>
  <img css={{"height": "70%", "width": "100%", "object-fit": "cover", "object-position": "center", "border-radius": "10px", "margin-bottom": "14px"}} src={`https://acmucsd.s3.us-west-1.amazonaws.com/portal/events/46f1a42e-41e5-4103-8052-74d3e13d6a62.png`}/>
  <RadixThemesFlex>
  <RadixThemesBox css={{"margin-bottom": "10px", "spacing": "1", "height": "100%"}}>
  <RadixThemesHeading as={`h1`} size={`5`} trim={`normal`}>
  {`ACM Kickoff`}
</RadixThemesHeading>
  <RadixThemesText as={`p`} size={`4`} trim={`normal`} weight={`medium`}>
  {`ACM @ UCSD`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"margin-bottom": "10px"}} size={`3`} trim={`normal`} weight={`light`}>
  {`UC San Diego`}
</RadixThemesText>
  <RadixThemesScrollArea>
  <RadixThemesFlex css={{"height": 55, "type": "always", "scrollbars": "vertical"}}>
  <RadixThemesText as={`p`} size={`2`} trim={`both`}>
  {`Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesScrollArea>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesBox>
  <RadixThemesText as={`p`} css={{"margin-bottom": "10px"}} size={`3`} trim={`normal`} weight={`light`}>
  {`This is the end of your events`}
</RadixThemesText>
</RadixThemesFlex>
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
  <Fragment_e4189cc831f29355b3c1176b62dd13e8/>
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
  {`Grasshopper`}
</title>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
