---
slug: "fi"
url: "/mobilnisite/slovnik/fi/"
type: "slovnik"
title: "FI – Format Identifier"
date: 2025-01-01
abbr: "FI"
fullName: "Format Identifier"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fi/"
summary: "Pole v protokolových datových jednotkách (PDU), které označuje strukturu a kódování následujících dat. Používá se ve vrstvách jako PDCP a MAC, aby umožnilo multiplexování, efektivní kompresi hlaviček"
---

FI je pole v protokolových datových jednotkách (PDU), které označuje strukturu a kódování následujících dat, aby umožnilo multiplexování, kompresi hlaviček a správnou interpretaci paketů v systémech 3GPP.

## Popis

Identifikátor formátu (FI) je klíčové pole v hlavičkách protokolů ve specifikacích 3GPP, používané primárně ve vrstvě Protokolu konvergence paketových dat ([PDCP](/mobilnisite/slovnik/pdcp/)) a řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), aby signalizovalo formát přidružené protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)). Jedná se o několik bitů (např. 2 bity v PDCP pro LTE/NR), které explicitně definují, jak mají být parsovány zbývající bity hlavičky a datové části. Například v datových PDU PDCP FI označuje, zda PDU obsahuje pořadové číslo, zda je přítomný kontext robustní komprese hlaviček ([ROHC](/mobilnisite/slovnik/rohc/)) a délku případných dalších polí. To umožňuje jedné protokolové entitě dynamicky podporovat více formátů PDU a přizpůsobovat se různým požadavkům služeb, jako je signalizace řídicí roviny, data uživatelské roviny nebo IP pakety s komprimovanou hlavičkou.

Z architektonického hlediska FI generuje vysílající protokolová entita (např. PDCP vysílač v UE nebo gNB) na základě konfigurace přijaté z vyšších vrstev nebo signalizace [RRC](/mobilnisite/slovnik/rrc/). V PDCP, specifikovaném v 3GPP TS 36.323 a TS 38.323, je FI součástí hlavičky PDCP PDU, která také obsahuje pole jako PDCP pořadové číslo ([SN](/mobilnisite/slovnik/sn/)) a data. Přijímající entita nejprve zkoumá bity FI, aby určila strukturu hlavičky, než se pokusí dekomprimovat nebo dešifrovat datovou část. V MAC, podle TS 36.321 a TS 38.321, indikátory podobné FI (např. formáty podhlaviček) identifikují přítomnost a velikost identifikátorů logických kanálů ([LCID](/mobilnisite/slovnik/lcid/)), pole délky a výplně, což umožňuje multiplexování více MAC servisních datových jednotek ([SDU](/mobilnisite/slovnik/sdu/)) do jednoho transportního bloku.

Operace zahrnuje nastavení FI vysílačem podle typu PDU: například '00' může označovat PDCP datové PDU s 12bitovým SN a bez ROHC zpětné vazby, zatímco '01' může označovat PDU s 7bitovým SN a polem ROHC zpětné vazby. Přijímač použije konečný automat nebo vyhledávací tabulku, jak je definováno ve specifikaci, k interpretaci FI a extrahování správných polí. Tento mechanismus je klíčový pro efektivní využití rádiových prostředků, protože se vyhýbá vysílání hlaviček pevné délky pro všechna PDU a místo toho používá minimální režii přizpůsobenou konkrétnímu kontextu. Také zajišťuje zpětnou a dopřednou kompatibilitu, protože nové hodnoty FI mohou být definovány v pozdějších vydáních pro zavedení nových formátů PDU bez narušení stávajících implementací.

## K čemu slouží

Identifikátor formátu byl zaveden, aby řešil potřebu flexibilního a efektivního formátování protokolových datových jednotek ve vyvíjejících se systémech 3GPP. Rané buněčné protokoly často používaly pevné struktury PDU, což vedlo k nepotřebné režii, když určitá pole (jako velká pořadová čísla nebo kompresní kontexty) nebyla potřebná pro všechny typy provozu. S příchodem LTE ve vydání 8, které podporovalo rozmanité služby od hlasu přes IP (VoIP) po vysokorychlostní internet, se stala nezbytnou adaptivnější struktura hlaviček pro optimalizaci využití rádiových prostředků a snížení latence.

Primární problém, který FI řeší, je efektivní multiplexování a zpracování heterogenních datových toků ve stejné protokolové vrstvě. Například v PDCP mohou některé pakety vyžadovat robustní kompresi hlaviček (ROHC) pro minimalizaci režie IP hlaviček, zatímco jiné (jako řídicí signalizace) ne. Bez FI by přijímač musel slepě zkoušet více metod parsování, což by zvyšovalo složitost a pravděpodobnost chyb. FI poskytuje explicitní signalizaci, která umožňuje přijímači správně a rychle zpracovat každé PDU, což je kritické pro služby s nízkou latencí a energeticky efektivní provoz zařízení.

Historicky FI navazuje na koncepty z dřívějších telekomunikačních a internetových protokolů (jako pole Type v Ethernetu), ale je přizpůsobeno jedinečným omezením bezdrátových spojů. Řešilo omezení v před-LTE systémech, kde byla režie protokolů méně optimalizovaná, což přispívalo k nižší spektrální efektivitě. V LTE a 5G NR FI umožňuje pokročilé funkce jako duplikace (pro spolehlivost), ochrana integrity a efektivní podpora malých datových paketů v IoT tím, že umožňuje odlišné formáty PDU pro každý případ použití. Jeho návrh umožňuje 3GPP vyvíjet protokoly napříč vydáními při zachování interoperability, protože zařízení mohou ignorovat neznámé hodnoty FI nebo je zpracovat šetrně podle předdefinovaných pravidel.

## Klíčové vlastnosti

- Explicitně označuje strukturu a délky polí protokolových datových jednotek (PDU)
- Umožňuje podporu více formátů PDU v rámci jedné protokolové entity (např. PDCP, MAC)
- Snižuje režii hlaviček tím, že umožňuje pole proměnné délky na základě kontextu
- Usnadňuje správné parsování hlaviček pro robustní kompresi hlaviček (ROHC) a číslování pořadí
- Podporuje dynamické přizpůsobení různým typům služeb (např. řídicí rovina, uživatelská rovina, IoT data)
- Zajišťuje dopřednou kompatibilitu tím, že umožňuje definici nových hodnot formátu v budoucích vydáních

## Související pojmy

- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [ROHC – Robust Header Compression](/mobilnisite/slovnik/rohc/)

## Definující specifikace

- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [FI na 3GPP Explorer](https://3gpp-explorer.com/glossary/fi/)
