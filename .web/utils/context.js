import { createContext, useContext, useMemo, useReducer, useState } from "react"
import { applyDelta, Event, hydrateClientStorage, useEventLoop, refs } from "/utils/state.js"

export const initialState = {"state": {"is_hydrated": false, "router": {"session": {"client_token": "", "client_ip": "", "session_id": ""}, "headers": {"host": "", "origin": "", "upgrade": "", "connection": "", "pragma": "", "cache_control": "", "user_agent": "", "sec_websocket_version": "", "sec_websocket_key": "", "sec_websocket_extensions": "", "accept_encoding": "", "accept_language": ""}, "page": {"host": "", "path": "", "raw_path": "", "full_path": "", "full_raw_path": "", "params": {}}}}, "state.update_vars_internal_state": {}, "state.state": {"user_id": "no userID"}, "state.global_state": {"authentication_session": null, "button_text": "Attend", "is_attending": false, "school_names": ["UC San Diego", "UC Santa Cruz", "UC Davis", "UCLA", "UC Merced", "UC Riverside", "UC Irvine", "UC Berkeley", "UC Santa Barbara"], "schools": [{"id": "1", "name": "UC San Diego"}, {"id": "9", "name": "UC Santa Cruz"}, {"id": "2", "name": "UC Davis"}, {"id": "3", "name": "UCLA"}, {"id": "7", "name": "UC Merced"}, {"id": "8", "name": "UC Riverside"}, {"id": "5", "name": "UC Irvine"}, {"id": "6", "name": "UC Berkeley"}, {"id": "4", "name": "UC Santa Barbara"}], "session_id": "", "token_info": {}, "token_is_valid": false, "user": null}, "state.on_load_internal_state": {}}

export const defaultColorMode = "light"
export const ColorModeContext = createContext(null);
export const UploadFilesContext = createContext(null);
export const DispatchContext = createContext(null);
export const StateContexts = {
  state: createContext(null),
  state__update_vars_internal_state: createContext(null),
  state__state: createContext(null),
  state__global_state: createContext(null),
  state__on_load_internal_state: createContext(null),
}
export const EventLoopContext = createContext(null);
export const clientStorage = {"cookies": {"state.global_state.session_id": {"name": "session_id", "path": "/", "maxAge": 3600, "sameSite": "lax"}}, "local_storage": {}}

export const state_name = "state"

// Theses events are triggered on initial load and each page navigation.
export const onLoadInternalEvent = () => {
    const internal_events = [];

    // Get tracked cookie and local storage vars to send to the backend.
    const client_storage_vars = hydrateClientStorage(clientStorage);
    // But only send the vars if any are actually set in the browser.
    if (client_storage_vars && Object.keys(client_storage_vars).length !== 0) {
        internal_events.push(
            Event(
                'state.update_vars_internal_state.update_vars_internal',
                {vars: client_storage_vars},
            ),
        );
    }

    // `on_load_internal` triggers the correct on_load event(s) for the current page.
    // If the page does not define any on_load event, this will just set `is_hydrated = true`.
    internal_events.push(Event('state.on_load_internal_state.on_load_internal'));

    return internal_events;
}

// The following events are sent when the websocket connects or reconnects.
export const initialEvents = () => [
    Event('state.hydrate'),
    ...onLoadInternalEvent()
]

export const isDevMode = true

export function UploadFilesProvider({ children }) {
  const [filesById, setFilesById] = useState({})
  refs["__clear_selected_files"] = (id) => setFilesById(filesById => {
    const newFilesById = {...filesById}
    delete newFilesById[id]
    return newFilesById
  })
  return (
    <UploadFilesContext.Provider value={[filesById, setFilesById]}>
      {children}
    </UploadFilesContext.Provider>
  )
}

export function EventLoopProvider({ children }) {
  const dispatch = useContext(DispatchContext)
  const [addEvents, connectErrors] = useEventLoop(
    dispatch,
    initialEvents,
    clientStorage,
  )
  return (
    <EventLoopContext.Provider value={[addEvents, connectErrors]}>
      {children}
    </EventLoopContext.Provider>
  )
}

export function StateProvider({ children }) {
  const [state, dispatch_state] = useReducer(applyDelta, initialState["state"])
  const [state__update_vars_internal_state, dispatch_state__update_vars_internal_state] = useReducer(applyDelta, initialState["state.update_vars_internal_state"])
  const [state__state, dispatch_state__state] = useReducer(applyDelta, initialState["state.state"])
  const [state__global_state, dispatch_state__global_state] = useReducer(applyDelta, initialState["state.global_state"])
  const [state__on_load_internal_state, dispatch_state__on_load_internal_state] = useReducer(applyDelta, initialState["state.on_load_internal_state"])
  const dispatchers = useMemo(() => {
    return {
      "state": dispatch_state,
      "state.update_vars_internal_state": dispatch_state__update_vars_internal_state,
      "state.state": dispatch_state__state,
      "state.global_state": dispatch_state__global_state,
      "state.on_load_internal_state": dispatch_state__on_load_internal_state,
    }
  }, [])

  return (
    <StateContexts.state.Provider value={ state }>
    <StateContexts.state__update_vars_internal_state.Provider value={ state__update_vars_internal_state }>
    <StateContexts.state__state.Provider value={ state__state }>
    <StateContexts.state__global_state.Provider value={ state__global_state }>
    <StateContexts.state__on_load_internal_state.Provider value={ state__on_load_internal_state }>
      <DispatchContext.Provider value={dispatchers}>
        {children}
      </DispatchContext.Provider>
    </StateContexts.state__on_load_internal_state.Provider>
    </StateContexts.state__global_state.Provider>
    </StateContexts.state__state.Provider>
    </StateContexts.state__update_vars_internal_state.Provider>
    </StateContexts.state.Provider>
  )
}