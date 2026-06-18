---
slug: "svn-mac"
url: "/mobilnisite/slovnik/svn-mac/"
type: "slovnik"
title: "SVN-MAC – SVN Medium Access Control label"
date: 2025-01-01
abbr: "SVN-MAC"
fullName: "SVN Medium Access Control label"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/svn-mac/"
summary: "Štítek používaný v architektuře Satellite Virtual Network (SVN) k identifikaci a správě prostředků nebo kontextů vrstvy Medium Access Control (MAC) pro satelitní připojení. Napomáhá směrování a správě"
---

SVN-MAC je štítek používaný v architektuře Satellite Virtual Network k identifikaci a správě prostředků vrstvy MAC (Medium Access Control) pro satelitní připojení, který napomáhá směrování a správě relací.

## Popis

Štítek [SVN](/mobilnisite/slovnik/svn/) Medium Access Control (SVN-MAC) je identifikátor definovaný ve specifikacích 3GPP pro operace v Satellite Virtual Network (SVN). Používá se k označení nebo odkazování na konkrétní kontexty, prostředky nebo entity vrstvy Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) spojené s připojením uživatelského zařízení (UE) přes satelitní přístupovou síť. Vrstva MAC je zodpovědná za řízení přístupu ke sdílenému satelitnímu rádiovému médiu, zpracování rámcování, adresování a řízení chyb. Štítek SVN-MAC poskytuje SVN a funkcím jádra sítě jednoznačný odkaz pro identifikaci a správu těchto instancí na vrstvě MAC během procedur, jako je zřizování relace, předávání spojení a modifikace prostředků.

Architektonicky štítek SVN-MAC funguje v signalizaci řídicí roviny mezi SVN a dalšími síťovými entitami, jako je Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)). Může být zahrnut v protokolových zprávách (např. přes rozhraní [N2](/mobilnisite/slovnik/n2/) nebo [S1-MME](/mobilnisite/slovnik/s1-mme/)) pro korelaci informací z vrstvy MAC s kontexty relací na vyšších vrstvách. Mezi klíčové komponenty patří SVN, které štítek generuje nebo přiřazuje na základě specifik satelitní přístupové sítě, a uzly jádra sítě, které jej mohou ukládat nebo na něj odkazovat pro rozhodnutí související s relací. Štítek pomáhá překlenout propast mezi satelitně specifickými procedurami MAC a obecnými protokoly jádra sítě 3GPP.

Princip fungování: Když se UE připojí přes satelit, satelitní přístupová síť alokuje prostředky na vrstvě MAC (jako je kontext plánování nebo identifikátor logického kanálu). SVN asociuje tyto prostředky se štítkem SVN-MAC a zahrne tento štítek do signalizačních zpráv směrem k jádru sítě během připojování nebo zřizování relace. Jádro sítě pak může tento štítek použít v následné komunikaci se SVN k odkazování na tento konkrétní kontext MAC, například při úpravě parametrů QoS nebo během fáze přípravy předání spojení. Tím je zajištěno, že příkazy související s řízením rádiových prostředků jsou přesně aplikovány na správný satelitní spoj UE. Jeho úlohou je poskytnout jednoznačný odkaz, který zlepšuje koordinaci mezi správou relací v jádru sítě a řízením rádiových prostředků v satelitní přístupové síti, což přispívá k efektivní mobilitě a využití prostředků v hybridních terestriálně-satelitních sítích.

## K čemu slouží

Štítek SVN-MAC byl zaveden, aby vyřešil potřebu přesné identifikace a správy prostředků vrstvy Medium Access Control v kontextu Satellite Virtual Networks. Protože satelitní spoje mají jedinečné charakteristiky na vrstvě [MAC](/mobilnisite/slovnik/mac/) – jako jsou odlišné algoritmy plánování, delší časové posuny a schémata sdíleného přístupu k médiu – vznikla potřeba standardizovaného způsobu, jak se na tyto specifické prostředky může jádro sítě odkazovat, aniž by muselo rozumět podrobnostem podkladového satelitního protokolu MAC. Předchozí přístupy mohly spoléhat na obecné identifikátory, které mohly vést k nejednoznačnostem, nebo vyžadovaly proprietární rozšíření.

Vytvořený ve 3GPP Release 11 řeší štítek SVN-MAC problém efektivní správy relací a mobility pro satelitně připojená UE tím, že poskytuje jasný, v rámci celé sítě platný identifikátor pro kontexty MAC. To umožňuje plynulejší předávání spojení, přesné vynucování QoS a lepší koordinaci prostředků mezi [SVN](/mobilnisite/slovnik/svn/) a jádrem sítě 3GPP. Motivace vycházela z pokročilejší integrace satelitního přístupu v pozdějších vydáních 3GPP, kde byly potřeba sofistikovanější řídicí mechanismy pro podporu pokročilých služeb a zajištění optimalizace výkonu přes náročné satelitní rádiové rozhraní.

## Klíčové vlastnosti

- Unikátní identifikátor pro kontexty na vrstvě MAC v rámci Satellite Virtual Network
- Používán v signalizaci řídicí roviny mezi SVN a funkcemi jádra sítě 3GPP
- Umožňuje korelaci mezi relacemi v jádru sítě a satelitními rádiovými prostředky
- Podporuje procedury jako předávání spojení, modifikace QoS a správa relací
- Umožňuje jádru sítě odkazovat se na satelitně specifické entity MAC bez detailní znalosti protokolu MAC
- Definován ve specifikaci 3GPP 24.229 pro architektury související se SVN

## Související pojmy

- [SVN – Satellite Virtual Network](/mobilnisite/slovnik/svn/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP

---

📖 **Anglický originál a plná specifikace:** [SVN-MAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/svn-mac/)
