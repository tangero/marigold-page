---
slug: "dlci"
url: "/mobilnisite/slovnik/dlci/"
type: "slovnik"
title: "DLCI – Data Link Connection Identifier"
date: 2025-01-01
abbr: "DLCI"
fullName: "Data Link Connection Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dlci/"
summary: "Číselný identifikátor, který jednoznačně identifikuje konkrétní spojení na datové vrstvě (Data Link Connection, DLC) v rámci protokolu datové vrstvy. Používá se pro multiplexování více logických spoje"
---

DLCI je číselný identifikátor, který jednoznačně identifikuje spojení na datové vrstvě (Data Link Connection) a umožňuje multiplexování více logických spojení přes jeden fyzický kanál pro směrování rámců.

## Popis

Identifikátor spojení na datové vrstvě (Data Link Connection Identifier, DLCI) je klíčové pole v hlavičce rámce datové vrstvy. Jeho primární funkcí je identifikovat logické spojení na datové vrstvě (Data Link Connection), ke kterému přenášený rámec patří. V systémech 3GPP se tento koncept významně používá v protokolech jako je Link Access Protocol on the Dm channel (LAPDm) pro GSM rozhraní rádiového přístupu a v některých protokolech pro přenos signalizace v jádru sítě. DLCI umožňuje, aby jediný fyzický prostředek (např. časový slot nebo signalizační propojení) současně přenášel rámce pro více nezávislých logických spojení, což je proces známý jako multiplexování.

Technicky je hodnota DLCI přiřazena během navazování spojení na datové vrstvě. V LAPDm (specifikovaném v TS 44.006) obsahuje adresní pole rámce DLCI, které se typicky skládá z identifikátoru přístupového bodu služby (Service Access Point Identifier, SAPI) a v některých formátech také z identifikátoru koncového bodu terminálu (Terminal Endpoint Identifier, TEI). SAPI identifikuje typ služby nebo entitu vrstvy 3 (např. řízení hovoru, správu mobility, SMS), která spojení používá, zatímco TEI identifikuje konkrétní terminál (jako je mobilní stanice) na vícebodovém spoji. Společně tvoří úplnou adresu pro logický spoj.

Když síťová entita přijme rámec, prozkoumá DLCI v adresním poli, aby určila, s kterým logickým spojením je rámec asociován. Rámec je poté předán odpovídající entitě datové vrstvy ke zpracování, které zahrnuje kontrolu čísel sekvence, provedení detekce chyb a konečně doručení obsažené informace správné entitě protokolu vrstvy 3 (např. [MM](/mobilnisite/slovnik/mm/), [CC](/mobilnisite/slovnik/cc/), [GMM](/mobilnisite/slovnik/gmm/)). Tento mechanismus je klíčový pro efektivní využití prostředků, protože se vyhýbá potřebě vyhrazených fyzických kanálů pro každý typ signalizace nebo datového toku. Správa hodnot DLCI, jejich přiřazování a mapování na vyšší vrstvy jsou ústřední pro fungování datové vrstvy v legacy sítích GSM/[GPRS](/mobilnisite/slovnik/gprs/).

## K čemu slouží

DLCI bylo vytvořeno k řešení problému efektivní podpory více souběžných komunikačních toků přes jediný, často vzácný, fyzický přenosový prostředek, zejména rádiový kanál v celulárních sítích. Bez takového identifikátoru by síť nebyla schopna rozlišit mezi rámci nesoucími různé typy informací (např. signál pro zřízení hovoru versus aktualizaci mobility) určené pro různé logické koncové body, což by vedlo k záměně a nesprávnému zpracování.

Jeho vývoj byl motivován standardem [ISDN](/mobilnisite/slovnik/isdn/) Q.921 ([LAPD](/mobilnisite/slovnik/lapd/)), který používal DLCI pro multiplexování více logických spojů na D-kanálu. 3GPP toto přizpůsobilo pro mobilní specifický protokol LAPDm. Primární problém, který řeší, je optimalizace prostředků; namísto alokace samostatných fyzických kanálů pro každou službu (což by bylo extrémně nehospodárné, zejména na rozhraní vzduch–rádio), může být jeden kanál sdílen časovým multiplexováním rámců označených různými DLCI.

Dále poskytuje jasný adresní mechanismus na vrstvě 2, který umožňuje funkci demultiplexování na přijímači. To umožňuje síti a mobilní stanici udržovat několik paralelních logických spojení pro různé účely – například jedno pro řízení hlasového hovoru, další pro SMS a další pro správu paketové datové relace – vše přes stejný fyzický rádiový spoj. Tato architektonická elegance a efektivita byly zásadní pro bohatost služeb GSM nad rámec prosté hlasové telefonie.

## Klíčové vlastnosti

- Jednoznačně identifikuje logické spojení na datové vrstvě (Data Link Connection) v rámci jednoho fyzického spoje nebo rozhraní.
- Umožňuje multiplexování více nezávislých logických kanálů přes jedinou fyzickou přenosovou cestu.
- Je součástí adresního pole rámce, často obsahující dílčí pole jako SAPI a TEI pro identifikaci služby a koncového bodu.
- Používá se přijímačem k nasměrování příchozího rámce ke správné entitě datové vrstvy a následně k příslušnému protokolu vrstvy 3.
- Hodnoty jsou přiřazovány během procedur navazování spojení.
- Nezbytné pro fungování protokolů vrstvy 2, jako je LAPDm v GSM.

## Související pojmy

- [DLC – Data Link Connection](/mobilnisite/slovnik/dlc/)
- [Multiplexing](/mobilnisite/slovnik/multiplexing/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 49.008** (Rel-19) — BSSAP on E-interface for inter-MSC handover

---

📖 **Anglický originál a plná specifikace:** [DLCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/dlci/)
