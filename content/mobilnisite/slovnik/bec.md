---
slug: "bec"
url: "/mobilnisite/slovnik/bec/"
type: "slovnik"
title: "BEC – Backward Error Correction"
date: 2025-01-01
abbr: "BEC"
fullName: "Backward Error Correction"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bec/"
summary: "Backward Error Correction (BEC) je technika používaná v GSM/EDGE rádiové přístupové síti (GERAN) pro zvýšení spolehlivosti přenosu dat. Zahrnuje detekci chyb přijímačem a žádost o opětovné vyslání poš"
---

BEC je technika používaná v síti GERAN pro zvýšení spolehlivosti dat, při níž přijímač detekuje chyby a vyžádá si od odesílatele opětovné vyslání poškozených dat.

## Popis

Backward Error Correction (BEC) je mechanismus řízení chyb definovaný v dokumentu 3GPP TS 43.064 pro GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiovou přístupovou síť ([GERAN](/mobilnisite/slovnik/geran/)). Funguje na vrstvě řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) a je klíčovou součástí protokolového zásobníku spojové vrstvy pro služby s přepojováním paketů, jako jsou [GPRS](/mobilnisite/slovnik/gprs/) a EDGE. BEC je v zásadě protokol typu Automatic Repeat Request ([ARQ](/mobilnisite/slovnik/arq/)), konkrétně mechanismus selektivního opakování (selective-repeat ARQ). Jeho hlavní funkcí je zajistit spolehlivé doručování datových bloků přes rozhraní vzduch–země prostřednictvím detekce a opravy přenosových chyb vznikajících vlivem faktorů, jako je interference, útlum a šum.

Protokol funguje v cyklickém procesu vysílání, potvrzování a případného opětovného vysílání. Odesílatel vysílá datové bloky, z nichž každý je označen pořadovým číslem. Příjímač kontroluje každý blok na chyby pomocí kontrolní sekvence rámce ([FCS](/mobilnisite/slovnik/fcs/)). Pokud je blok přijat správně, přijímač odešle odesílateli kladné potvrzení ([ACK](/mobilnisite/slovnik/ack/)). Pokud je detekována chyba, přijímač zavrhne poškozený blok a odešle záporné potvrzení ([NACK](/mobilnisite/slovnik/nack/)) nebo v některých implementacích prostě neodešle ACK. Odesílatel udržuje vyrovnávací paměť pro opětovné vysílání. Po přijetí NACK nebo po uplynutí časového limitu bez ACK znovu vysílá konkrétní datový blok identifikovaný jeho pořadovým číslem. Toto selektivní opětovné vysílání je efektivnější než protokoly typu go-back-N, protože znovu vysílá pouze chybné bloky, nikoli všechny následující.

Mezi klíčové architektonické komponenty patří vysílací entita RLC, přijímací entita RLC, schéma číslování sekvencí, signalizace potvrzení (ACK/NACK) a časovač pro opětovné vysílání. BEC funguje ve spojení s dopřednou korekcí chyb (FEC) na fyzické vrstvě. Zatímco FEC přidává redundantní bity pro automatickou opravu omezeného počtu chyb, BEC řeší případy chyb přesahující možnosti FEC. Tento hybridní přístup poskytuje robustní obranu proti různým podmínkám na kanálu. Parametry protokolu, jako je velikost okna (určující povolený počet nepotvrzených bloků) a hodnoty časovačů, jsou konfigurovatelné pro vyvážení propustnosti a zpoždění v závislosti na podmínkách sítě.

V celkové architektuře GERAN je BEC klíčový pro protokol řízení rádiového spoje / řízení přístupu k médiu (RLC/MAC). Zajišťuje, že nespolehlivý fyzický rádiový spoj se horním vrstvám (LLC a výše) jeví jako spolehlivý datový kanál. Tato spolehlivost je zásadní pro aplikace založené na TCP/IP běžící přes GPRS/EDGE, protože zabraňuje vrstvě TCP v nesprávné interpretaci ztráty paketů na rádiové vrstvě jako přetížení sítě, což by spustilo zbytečné a škodlivé mechanismy řízení zahlcení. BEC tedy hraje zásadní roli při udržování efektivní a předvídatelné kvality datových služeb.

## K čemu slouží

BEC byl zaveden k řešení základní výzvy poskytování spolehlivých datových služeb přes inherentně náchylné k chybám GSM rádiové rozhraní. Rané hlasové služby s přepojováním okruhů používaly FEC, ale pro paketová data (GPRS) byl potřeba efektivnější a robustnější mechanismus řízení chyb. Primární problém, který BEC řeší, je spolehlivý přenos datových paketů navzdory vysoké a proměnlivé míře bitových chyb (BER) na bezdrátovém kanálu. Bez něj by protokoly vyšších vrstev byly zatíženy nadměrnou ztrátou paketů, což by vedlo ke špatnému výkonu aplikací a neefektivnímu využití síťových prostředků.

Motivace pro vytvoření BEC vycházela z vývoje GSM na síť schopnou přenášet data s GPRS. Čisté schémata FEC vyžadují přidání významné redundance do každého přenosu, což spotřebovává cennou šířku pásma i za dobrých podmínek na kanálu. Pro trhaný datový provoz je to neefektivní. BEC jako schéma ARQ spotřebovává dodatečnou šířku pásma (pro opětovná vysílání) pouze tehdy, když k chybám skutečně dojde. To jej z hlediska využití spektra činí efektivnějším pro typické datové vzorce. Byl navržen tak, aby fungoval ve spolupráci se stávajícím FEC, čímž vytváří vrstvenou obranu: FEC opravuje časté, malé chyby, zatímco BEC obnovuje data po méně častých, ale rozsáhlejších chybových shlucích.

Historicky BEC poskytl standardizovanou, optimalizovanou metodu pro obnovu po chybách, která byla přizpůsobena časování a struktuře rámců systému GSM/GERAN. Řešil omezení jednodušších schémat ARQ implementací selektivního opakování, které zlepšuje propustnost na spojích s vyšší latencí nebo vyšší mírou chyb ve srovnání s ARQ typu stop-and-wait nebo go-back-N. Jeho návrh byl klíčový pro umožnění komerční životaschopnosti služeb mobilního internetu a zasílání zpráv na sítích 2G a 2.5G a položil základy konceptům později zdokonaleným v 3G UMTS a 4G LTE.

## Klíčové vlastnosti

- Mechanismus selektivního opakování ARQ pro efektivní opětovná vysílání
- Funguje na vrstvě RLC v protokolovém zásobníku GERAN
- Používá pořadová čísla a signalizaci ACK/NACK pro řízení chyb
- Pracuje ve spojení s dopřednou korekcí chyb (FEC) na fyzické vrstvě
- Konfigurovatelné parametry, jako je velikost okna a časovače, pro ladění výkonu
- Zajišťuje spolehlivý datový kanál pro protokoly vyšších vrstev, jako je TCP/IP

## Související pojmy

- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [FEC – Forward Erasure Correction / Forward Error Correction](/mobilnisite/slovnik/fec/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [BEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bec/)
