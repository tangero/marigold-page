---
slug: "hps"
url: "/mobilnisite/slovnik/hps/"
type: "slovnik"
title: "HPS – Handover Path Switching"
date: 2025-01-01
abbr: "HPS"
fullName: "Handover Path Switching"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hps/"
summary: "Handover Path Switching (HPS) je základní procedura správy mobility v páteřní síti, která přesměrovává datovou cestu uživatele během předávání spojení mezi základnovými stanicemi nebo přístupovými tec"
---

HPS je procedura v páteřní síti, která přesměrovává datovou cestu uživatele během předávání spojení aktualizací směrovacích kotvů a koncových bodů tunelů, aby zajistila plynulou kontinuitu služby.

## Popis

Handover Path Switching (HPS) je základní proces v rámci architektury správy mobility 3GPP, zodpovědný za znovunastavení datové cesty v uživatelské rovině, když uživatelské zařízení (UE) přechází z jedné buňky nebo rádiové přístupové technologie ([RAT](/mobilnisite/slovnik/rat/)) na jinou. Z architektonického hlediska zahrnuje koordinaci mezi rádiovou přístupovou sítí (RAN), řídicí rovinou páteřní sítě (např. [MME](/mobilnisite/slovnik/mme/) v 4G, [AMF](/mobilnisite/slovnik/amf/) v 5G) a bránami uživatelské roviny (např. [S-GW](/mobilnisite/slovnik/s-gw/)/[P-GW](/mobilnisite/slovnik/p-gw/) v 4G, [UPF](/mobilnisite/slovnik/upf/) v 5G). Procedura funguje tak, že zdrojový síťový uzel zahájí požadavek na předání spojení, což spustí cílový uzel a páteřní síť k vytvoření nových kontextů přenosu (bearer) nebo [PDU](/mobilnisite/slovnik/pdu/) relací a k modifikaci stávajících tak, aby data byla směrována novou cestou.

Mezi klíčové komponenty patří zdrojová a cílová základnová stanice ([eNB](/mobilnisite/slovnik/enb/)/gNB), entita správy mobility a obsluhující brána a brána paketové datové sítě. Proces typicky zahrnuje několik kroků: přípravu předání spojení (alokace zdrojů v cíli), provedení (UE se připojí k cíli) a dokončení (přepnutí cesty a uvolnění starých zdrojů). Kritickou akcí je 'Path Switch Request' (žádost o přepnutí cesty) odeslaná cílovým RAN uzlem do páteřní sítě, která instruuje brány uživatelské roviny, aby přepnuly datovou cestu pro downlink ze zdrojového na cílový uzel. Tím se aktualizují koncové body GTP tunelů, což zajišťuje doručování datových paketů na novou polohu UE bez přerušení relace.

Úlohou HPS je minimalizovat ztrátu paketů a latenci během událostí mobility. Podporuje různé typy předání spojení, včetně intra-RAT, inter-RAT a mezisystémových předání. Procedura je těsně integrována s dalšími mechanismy mobility, jako je aktualizace oblasti sledování (Tracking Area Update), a je v pozdějších vydáních optimalizována pro funkce jako duální konektivita, kde může být současně udržováno více datových cest. Efektivní HPS je klíčový pro kvalitu uživatelského zážitku u služeb v reálném čase, jako je hlas a video, protože přímo ovlivňuje dobu přerušení při předání spojení.

## K čemu slouží

HPS byl vyvinut, aby vyřešil základní výzvu udržení aktivních datových relací během mobility uživatele v celulárních sítích. Rané celulární systémy měly jednodušší předání spojení typu 'přeruš a pak vytvoř' (break-before-make), která způsobovala znatelné přerušení služby. Jak se sítě vyvíjely, aby podporovaly paketově přepínaná data a služby v reálném čase přes IP, jako je VoIP, stal se požadavek na plynulá předání spojení typu 'vytvoř a pak přeruš' (make-before-break) kritický. HPS poskytuje standardizovanou proceduru páteřní sítě pro efektivní přesměrování datových toků, která je základem plynulé mobility.

K jeho vytvoření vedla potřeba jednotné metody, nezávislé na přístupové technologii, pro správu cesty v uživatelské rovině během událostí mobility napříč stále více heterogenními sítěmi (2G/3G/4G/5G, ne-3GPP). Před jeho formalizací mohlo být řízení cesty specifické pro dodavatele a méně efektivní. HPS standardizuje signalizaci mezi RAN a páteřní sítí pro koordinaci přepnutí, čímž zajišťuje interoperabilitu a optimalizuje využití síťových zdrojů včasným uvolněním staré cesty. Řeší problémy kontinuity relace, snížení ztráty dat a efektivní využití přenosových kapac backhaulu a zdrojů páteřní sítě během kritické fáze předání spojení, což je nezbytné pro podporu mobilního broadbandu a služeb s nízkou latencí.

## Klíčové vlastnosti

- Standardizovaná procedura pro aktualizaci směrování v uživatelské rovině během intra- a inter-RAT předání spojení
- Minimalizuje ztrátu paketů a dobu přerušení při předání spojení prostřednictvím koordinovaného přepnutí cesty
- Zahrnuje klíčové síťové funkce: RAN uzly, správce mobility a brány uživatelské roviny
- Využívá žádosti o modifikaci GTP tunelů k přesměrování datových toků
- Podporuje plynulou kontinuitu služby pro aktivní datové relace
- Integruje se s širšími procedurami správy mobility a správy relací

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.960** (Rel-4) — UMTS Mobile Multimedia Technical Challenges

---

📖 **Anglický originál a plná specifikace:** [HPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/hps/)
