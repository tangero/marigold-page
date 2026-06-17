---
slug: "ands"
url: "/mobilnisite/slovnik/ands/"
type: "slovnik"
title: "ANDS – Access Network Discovery and Selection"
date: 2025-01-01
abbr: "ANDS"
fullName: "Access Network Discovery and Selection"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ands/"
summary: "ANDS je mechanismus 3GPP umožňující zařízením objevovat a vybírat vhodné přístupové sítě na základě politik operátora a preferencí uživatele. Poskytuje inteligentní výběr sítě nad rámec jednoduché síl"
---

ANDS je mechanismus 3GPP umožňující zařízením objevovat a vybírat vhodné přístupové sítě na základě politik operátora a preferencí uživatele pro inteligentní vícepřístupovou konektivitu.

## Popis

Access Network Discovery and Selection (ANDS) je komplexní rámec definovaný ve specifikacích 3GPP, který umožňuje uživatelskému zařízení (UE) objevovat dostupné přístupové sítě a činit inteligentní rozhodnutí o výběru na základě více kritérií. Mechanismu funguje kombinací politik poskytovaných sítí, možností UE a preferencí uživatele za účelem určení nejvhodnější přístupové sítě pro konkrétní služby nebo aplikace. ANDS je obzvláště důležitý v sítích 5G, kde koexistuje více technologií rádiového přístupu (RAT), včetně technologií 3GPP jako 5G NR, LTE a nepřístupů mimo 3GPP, jako je Wi-Fi a pevné sítě.

Architektura ANDS zahrnuje několik klíčových komponent spolupracujících dohromady. Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) je hlavní síťový prvek, který poskytuje informace o objevování a výběrové politiky UE. Tyto politiky jsou doručovány prostřednictvím ANDSF Management Objects (MOs) za použití protokolu [OMA](/mobilnisite/slovnik/oma/) Device Management. UE obsahuje klienta ANDSF, který tyto politiky přijímá, ukládá a aplikuje. Politiky mohou zahrnovat pravidla založená na poloze, čase, stavu roamingu, typu služby a stavu sítě. ANDS podporuje procedury objevování iniciované sítí i UE, což umožňuje flexibilní provoz v závislosti na síťových podmínkách a požadavcích UE.

ANDS funguje prostřednictvím hierarchické struktury politik, kde mají přednost politiky definované operátorem, ale jsou zohledňovány i preference uživatele a možnosti zařízení. Systém podporuje více typů politik včetně politik mezisystémové mobility ([ISMP](/mobilnisite/slovnik/ismp/)) pro výběr jediného aktivního přístupu, politik mezisystémového směrování ([ISRP](/mobilnisite/slovnik/isrp/)) pro současnou vícepřístupovou konektivitu a informací o objevování dostupných sítí. Tyto politiky jsou typicky vyjádřeny pomocí šablon založených na XML a mohou být dynamicky aktualizovány na základě měnících se síťových podmínek nebo požadavků operátora. UE vyhodnocuje tyto politiky vůči současným podmínkám, aby učinila optimální rozhodnutí o výběru přístupu.

Technická implementace zahrnuje několik protokolových vrstev a rozhraní. Referenční bod S14 mezi ANDSF a UE je používán pro doručování a správu politik. ANDS se integruje se stávajícími procedurami 3GPP včetně připojování, aktualizací oblasti sledování a procesů předávání. Systém podporuje provoz v režimu pull (UE vyžádá politiky) i push (síť zasílá politiky UE). Bezpečnostní mechanismy zajišťují integritu a autenticitu politik prostřednictvím autentizace a šifrování. ANDS také podporuje služby založené na poloze prostřednictvím integrace s polohovacími systémy, což umožňuje geograficky podložená rozhodnutí o výběru sítě.

V praktickém nasazení ANDS umožňuje sofistikované scénáře výběru sítě, jako je směrování provozu na Wi-Fi, je-li dostupná pro datově náročné aplikace, při zachování hlasových služeb na celulárních sítích, nebo výběr 5G NR pro služby ultra-spolehlivé nízkolatenční komunikace (URLLC) při použití LTE pro best-effort provoz. Flexibilita systému umožňuje operátorům implementovat komplexní strategie správy provozu, optimalizovat vyrovnávání zatížení sítě a zlepšovat uživatelský zážitek prostřednictvím inteligentního výběru přístupu, který zohledňuje jak technické parametry, tak obchodní cíle.

## K čemu slouží

ANDS byl vytvořen, aby řešil rostoucí složitost výběru sítě v heterogenním bezdrátovém prostředí, kde koexistuje více přístupových technologií. Před ANDS byl výběr sítě primárně založen na jednoduchých kritériích, jako je síla signálu nebo ruční výběr uživatelem, což často vedlo k neoptimálnímu využití sítě a špatnému uživatelskému zážitku. Rozšíření Wi-Fi sítí vedle celulárních sítí vytvořilo výzvy pro plynulou mobilitu a efektivní využití zdrojů. Operátoři potřebovali mechanismus pro inteligentní směrování provozu přes různé přístupové sítě na základě požadavků služeb, stavu sítě a obchodních politik.

Historický kontext vývoje ANDS zahrnuje vývoj od sítí s jedinou RAT k vícepřístupovým prostředím. Rané celulární sítě (2G/3G) měly omezené možnosti spolupráce se sítěmi mimo 3GPP. Jak se Wi-Fi stala všudypřítomnou a byly nasazovány sítě 4G/LTE, rostla potřeba integrovaného řízení přístupu. ANDS byl poprvé představen ve 3GPP Release 8 jako součást architektury Evolved Packet System (EPS), čímž poskytl standardizovaný rámec pro objevování a výběr přístupové sítě, který mohl být rozšiřován s příchodem nových přístupových technologií.

ANDS řeší několik kritických problémů v moderních bezdrátových sítích. Umožňuje operátorům implementovat politiky směrování provozu, které optimalizují využití síťových zdrojů napříč různými přístupovými technologiemi. Podporuje plynulou kontinuitu služeb při pohybu mezi různými přístupovými sítěmi. Systém řeší výzvu inteligentního výběru sítě v roamingových scénářích, kde může být k dispozici více navštívených sítí. ANDS také poskytuje mechanismy pro upřednostnění přístupu k nouzovým službám a podporuje regulatorní požadavky na dostupnost sítě. Poskytnutím standardizovaného rámce ANDS umožňuje interoperabilitu mezi implementacemi různých dodavatelů a zajišťuje konzistentní uživatelský zážitek napříč různými síťovými nasazeními.

## Klíčové vlastnosti

- Výběr přístupové sítě založený na politikách s využitím pravidel definovaných operátorem
- Podpora více typů politik včetně ISMP a ISRP
- Dynamické doručování a aktualizace politik prostřednictvím ANDSF
- Integrace s polohovými službami pro geograficky podložený výběr
- Podpora technologií přístupu 3GPP i mimo 3GPP
- Mechanismy pro upřednostnění přístupu k nouzovým službám

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)

## Definující specifikace

- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3

---

📖 **Anglický originál a plná specifikace:** [ANDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ands/)
