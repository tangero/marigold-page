---
slug: "efs"
url: "/mobilnisite/slovnik/efs/"
type: "slovnik"
title: "EFS – Effective File Size"
date: 2025-01-01
abbr: "EFS"
fullName: "Effective File Size"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/efs/"
summary: "Effective File Size (EFS) je metrika používaná ve specifikacích 3GPP, zejména v souvislosti se službou Multimedia Broadcast/Multicast Service (MBMS), která představuje velikost souboru nebo datové jed"
---

EFS je vypočítaná velikost souboru nebo datové jednotky v MBMS po zahrnutí dopředné korekce chyb a režie protokolů, což představuje skutečné rádiové zdroje potřebné pro spolehlivé doručení.

## Popis

Effective File Size (EFS) je parametr definovaný v kontextu služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) konsorcia 3GPP a potenciálně dalších mechanismů doručování dat. Nejde o skutečnou velikost souboru v bajtech, ale o odvozenou metriku, která představuje celkový objem dat, který musí být přenesen přes rádiové rozhraní, aby bylo původní obsah souboru doručen se specifikovanou úrovní spolehlivosti. Výpočet EFS zahrnuje původní velikost souboru a přidává veškerou potřebnou režii vyžadovanou pro přenos.

Hlavními složkami přidanými k původní velikosti souboru pro výpočet EFS jsou data parity pro dopřednou korekci chyb ([FEC](/mobilnisite/slovnik/fec/)) a hlavičky různých protokolových vrstev. V MBMS jsou soubory nebo datové jednotky často doručovány pomocí protokolu File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)) nad protokolem User Datagram Protocol ([UDP](/mobilnisite/slovnik/udp/)) a Internet Protocol (IP). Každá vrstva přidává svou vlastní hlavičku (FLUTE, UDP, IP). Dále, pro potlačení chyb v broadcastovém kanálu, je použita dopředná korekce chyb na aplikační vrstvě ([AL-FEC](/mobilnisite/slovnik/al-fec/)), typicky využívající kódy Raptor nebo RaptorQ podle specifikace 3GPP TS 26.346. Schéma AL-FEC generuje opravné symboly, které jsou vysílány spolu se zdrojovými symboly, čímž se zvyšuje celkový objem dat. EFS je součtem zdrojových symbolů (odvozených z původního souboru a protokolových hlaviček) a opravných symbolů.

EFS je klíčový parametr pro plánování a provoz sítě. Pro plánování přenosů v MBMS síť potřebuje znát EFS, aby určila, kolik rádiových zdrojů (např. kolik přenosových časových intervalů) musí být alokováno pro vysílání souboru v požadovaném časovém okně. Přímo souvisí s požadovanou datovou rychlostí a dosažitelnou pokrytou oblastí pro daný modulační a kódovací schéma. Použitím EFS mohou plánovači sítě přesně dimenzovat kapacitu přenosového kanálu MBMS a vytvářet efektivní přenosové plány, které zajišťují spolehlivý příjem na okraji buňky, kde jsou podmínky kanálu nejhorší a je potřeba nejvíce režie FEC.

## K čemu slouží

EFS byl definován, aby řešil praktický problém alokace zdrojů pro spolehlivé broadcastové/multicastové doručování souborů v mobilních sítích. Pouhé použití původní velikosti souboru je pro rádiové plánování nedostatečné, protože systém musí přidat významnou režii pro korekci chyb a protokolovou enkapsulaci, aby zajistil správný příjem souborů všemi uživateli v pokryté oblasti i přes proměnlivé rádiové podmínky. Bez standardizovaného způsobu, jak tuto režii zohlednit, by bylo plánování přenosů neefektivní nebo nespolehlivé.

Tento koncept vznikl se standardizací [MBMS](/mobilnisite/slovnik/mbms/), jehož cílem bylo doručovat obsah, jako jsou aktualizace softwaru, zpravodajské kanály nebo video klipy, mnoha uživatelům současně. Tradiční protokoly pro opakovaný přenos typu point-to-point (unicast) jsou pro tento účel neefektivní. MBMS využívá broadcast typu one-to-many s [AL-FEC](/mobilnisite/slovnik/al-fec/) pro spolehlivost. EFS poskytuje jednotnou metriku, která zahrnuje celkové náklady na rádiové zdroje potřebné pro doručení souboru, což umožňuje automatizované a optimální plánovací algoritmy. Řeší problém převodu požadavku na služební vrstvě (doručit soubor X) na požadavek na rádiové zdroje (alokovat Y fyzických bloků zdrojů).

Umožňuje poskytovatelům obsahu a síťovým operátorům mít společnou představu o spotřebě zdrojů pro daný kus obsahu. To je nezbytné pro správu kapacity, smlouvy o úrovni služeb a efektivní využití broadcastové nosné. EFS překlenuje propast mezi aplikační vrstvou a vrstvou rádiových zdrojů v broadcastových službách.

## Klíčové vlastnosti

- Představuje celkovou velikost pro rádiový přenos včetně režie FEC a protokolů
- Klíčový vstupní parametr pro plánovací algoritmy broadcastových přenosů MBMS
- Zahrnuje režii ze schémat AL-FEC, jako jsou Raptor kódy
- Započítává protokolové hlavičky z vrstev FLUTE, UDP a IP
- Umožňuje přesnou alokaci rádiových zdrojů pro služby doručování souborů
- Standardizovaná metrika pro plánování kapacity broadcastových přenosových kanálů

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.925** (Rel-4) — UMTS QoS and Network Performance Parameters
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [EFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/efs/)
