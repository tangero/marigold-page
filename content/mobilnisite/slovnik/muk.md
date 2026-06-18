---
slug: "muk"
url: "/mobilnisite/slovnik/muk/"
type: "slovnik"
title: "MUK – Multicast User Key"
date: 2025-01-01
abbr: "MUK"
fullName: "Multicast User Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/muk/"
summary: "Bezpečnostní klíč používaný ve službě Multimedia Broadcast Multicast Service (MBMS) pro šifrování provozu konkrétní multicastové/broadcastové služby. Zajišťuje, že obsah mohou dešifrovat a spotřebováv"
---

MUK je bezpečnostní klíč používaný v MBMS pro šifrování vysílaného provozu, který zajišťuje, že obsah mohou dešifrovat a spotřebovávat pouze autorizovaní účastníci, kteří si službu zakoupili.

## Popis

Multicast User Key (MUK) je kryptografický klíč klíčový pro zabezpečení služby na úrovni služby u Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a jejího vývoje evolved MBMS (eMBMS). Jedná se o službě specifický klíč používaný k šifrování skutečného multimediálního obsahu (MBMS provozu) doručovaného přes broadcast/multicast přenos. Každá samostatná MBMS služba (např. konkrétní [TV](/mobilnisite/slovnik/tv/) kanál nebo relace pro doručení souboru) je šifrována svým vlastním jedinečným MUK. To zajišťuje důvěrnost a řízení přístupu na úrovni služby.

MUK je součástí hierarchie klíčů definované v bezpečnostní architektuře MBMS. Je odvozen z nebo spojen se služebním klíčem nazývaným MBMS Service Key ([MSK](/mobilnisite/slovnik/msk/)). MSK je bezpečně doručen autorizovaným uživatelským zařízením (UE) prostřednictvím signalizace point-to-point za použití stávajících unicastových bezpečnostních mechanismů (zakořeněných v [USIM](/mobilnisite/slovnik/usim/)). UE následně použije MSK k odvození nebo získání odpovídajícího MUK pro službu, kterou je oprávněno přijímat. Samotný MUK je pak použit dešifrovacím engine UE k dešifrování šifrovaného textu přijatého přes broadcastové rozhraní na Multicast Traffic Channel ([MTCH](/mobilnisite/slovnik/mtch/)).

Na straně sítě je za oznámení služby, správu klíčů a šifrování obsahu zodpovědný [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Center). BM-SC vygeneruje nebo získá MUK pro službu, použije jej k zašifrování obsahových streamů a spravuje distribuci přidruženého MSK na [GAA](/mobilnisite/slovnik/gaa/) (Generic Authentication Architecture) server nebo přímo na UE účastníků prostřednictvím MBMS Key Distribution Center. Šifrování typicky používá standardizované algoritmy, jako je Advanced Encryption Standard ([AES](/mobilnisite/slovnik/aes/)).

Použití MUK umožňuje flexibilní obchodní modely. Operátor sítě může vysílat více služeb (některé zdarma, některé prémiové) přes stejnou geografickou oblast. Pouze UE, která disponují správným MUK pro prémiovou službu, ji mohou dešifrovat. To umožňuje modely typu pay-TV přes celulární broadcastové sítě. MUK může být pravidelně měněn (např. měsíčně u předplatného nebo na událost u pay-per-view) pro zvýšení bezpečnosti a správu období předplatného, přičemž nové klíče jsou doručovány prostřednictvím mechanismu MSK.

## K čemu slouží

MUK byl vytvořen k vyřešení zásadní obchodní a bezpečnostní výzvy broadcastových/multicastových služeb přes celulární sítě: jak monetizovat obsah. Na rozdíl od unicastu, kde existuje vyhrazené, zabezpečené spojení ke každému uživateli, broadcast vysílá stejná data všem uživatelům v buňce. Bez šifrování by jakékoli UE mohlo přijímat prémiový obsah zdarma. MUK poskytuje nezbytné řízení přístupu, které zajišťuje, že obsah mohou dešifrovat pouze platící účastníci.

Řeší omezení jednoduchého zabezpečení přístupu k síti. Zatímco UE musí být autentizováno, aby se připojilo k síti, toto neřídí přístup ke konkrétním broadcastovým službám. MUK zavádí samostatnou bezpečnostní vrstvu na úrovni služby. To bylo klíčové pro přijetí MBMS, protože poskytovatelé obsahu (jako mediální společnosti) by nenabízeli cenný obsah bez robustního mechanismu na ochranu svých příjmových toků.

Navíc systém MUK jako součást bezpečnostního rámce MBMS specifikovaného v 3GPP TS 33.246 umožňuje sofistikované servisní modely. Umožňuje různé služební klíče pro různé skupiny uživatelů (např. různé úrovně předplatného), regionální blackouty a časově omezený přístup. Vytvoření MUK a jeho přidružené hierarchie klíčů umožnilo celulárnímu broadcastu konkurovat tradičním broadcastovým médiím (jako je satelitní TV) nabídkou ekvivalentní ochrany obsahu, což motivovalo vývoj a nasazení eMBMS pro služby jako LTE Broadcast a 5G Broadcast.

## Klíčové vlastnosti

- Službě specifický šifrovací klíč pro MBMS/eMBMS provoz.
- Součást hierarchie klíčů odvozených z nebo spojených s MBMS Service Key (MSK).
- Používá se k šifrování obsahu na Multicast Traffic Channel (MTCH).
- Umožňuje modely podmíněného přístupu a obchodní modely typu pay-per-view/předplatné.
- Spravován a distribuován BM-SC a Key Distribution Center.
- Lze pravidelně aktualizovat k vynucení období předplatného a zvýšení bezpečnosti.

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.246** (Rel-19) — MBMS Security Specification
- **TR 33.850** (Rel-17) — 5G MBS Security Study
- **TS 33.888** (Rel-12) — Security Study for Group Communication in LTE

---

📖 **Anglický originál a plná specifikace:** [MUK na 3GPP Explorer](https://3gpp-explorer.com/glossary/muk/)
