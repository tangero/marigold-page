---
slug: "nt-hs-dpcch"
url: "/mobilnisite/slovnik/nt-hs-dpcch/"
type: "slovnik"
title: "NT-HS-DPCCH – NodeB Triggered High-Speed Dedicated Physical Control Channel"
date: 2025-01-01
abbr: "NT-HS-DPCCH"
fullName: "NodeB Triggered High-Speed Dedicated Physical Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nt-hs-dpcch/"
summary: "Mechanismus v UMTS/HSPA, který umožňuje NodeB (základnové stanici) spustit vysílání HS-DPCCH z UE za účelem zvýšení efektivity řídicí signalizace v uplinku. Optimalizuje využití prostředků tím, že umo"
---

NT-HS-DPCCH je mechanismus v UMTS/HSPA, při kterém NodeB spouští vysílání vysokorychlostního vyhrazeného fyzického řídicího kanálu (High-Speed Dedicated Physical Control Channel) ze strany UE za účelem zlepšení efektivity uplinku prostřednictvím odesílání řídicích informací na vyžádání.

## Popis

NodeB Triggered [HS-DPCCH](/mobilnisite/slovnik/hs-dpcch/) (NT-HS-DPCCH) je funkce v rámci architektury UMTS High-Speed Packet Access ([HSPA](/mobilnisite/slovnik/hspa/)), konkrétně definovaná ve specifikaci 3GPP TS 25.214. Týká se uplinkového řídicího kanálu HS-DPCCH, který přenáší klíčové zpětnovazební informace z uživatelského zařízení (UE) do NodeB, včetně indikátoru kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), potvrzení hybridního [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/) [ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)) a informací pro řízení předkódování ([PCI](/mobilnisite/slovnik/pci/)) pro MIMO operace. Tradičně je HS-DPCCH vysílán nepřetržitě, kdykoli je UE ve stavu CELL_DCH a nakonfigurováno pro HSDPA, což vede k trvalé režii uplinkové signalizace, i když je aktivita downlinkových dat nízká.

NT-HS-DPCCH zavádí spouštěný režim provozu. V tomto režimu může NodeB dynamicky přikázat UE, aby začalo nebo přestalo vysílat HS-DPCCH. Toho je dosaženo prostřednictvím downlinkové signalizace, typicky pomocí HS-SCCH příkazů. Když NodeB předpokládá nebo plánuje přenos downlinkových dat, odešle aktivační příkaz, který vyzve UE, aby začalo vysílat HS-DPCCH a poskytlo potřebnou zpětnou vazbu (CQI, HARQ ACK). Jakmile je přenos datové dávky dokončen, může NodeB vydat deaktivační příkaz, načež UE ukončí vysílání HS-DPCCH, čímž utlumí uplinkový řídicí kanál.

Architektura zahrnuje vylepšení protokolů vrstvy MAC jak na straně NodeB, tak UE pro interpretaci a provádění těchto aktivačních/deaktivačních příkazů. Scheduler v NodeB musí nyní při plánování downlinkových přenosů zohledňovat stav NT-HS-DPCCH, protože potřebuje zajistit, aby byl zpětnovazební kanál UE aktivní před odesláním dat. Toto přidává vrstvu koordinace, ale přináší významné systémové výhody. Klíčovými komponentami jsou fyzická vrstva UE pro zpracování HS-DPCCH, HSDPA scheduler v NodeB a signalizační protokol pro HS-SCCH příkazy.

Jeho úlohou v síti je zvýšit efektivitu využití uplinkových prostředků a snížit celkové rušení. Minimalizací období zbytečného vysílání HS-DPCCH snižuje spotřebu výkonu UE v uplinku, čímž prodlužuje životnost baterie, a snižuje nárůst šumu v uplinku buňky, což může zlepšit kapacitu pro ostatní uživatele. Představuje krok směrem k více síťově řízené signalizaci na vyžádání, která optimalizuje výkon pro přerušovaný paketový datový provoz typický pro HSPA sítě.

## K čemu slouží

NT-HS-DPCCH byl zaveden, aby řešil neefektivity spojené s nepřetržitým vysíláním HS-DPCCH v HSPA sítích. Ve standardním provozu by UE ve stavu CELL_DCH vysílalo HS-DPCCH nepřetržitě, kdykoli bylo nakonfigurováno pro HSDPA, bez ohledu na to, zda byly přenášena downlinková data. To vedlo k několika problémům: neustálému uplinkovému rušení generovanému řídicími kanály od všech aktivních UE, zbytečné spotřebě výkonu na straně UE vyčerpávající baterii a neefektivnímu využití uplinkových kódových a výkonových prostředků.

Historický kontext představuje vývoj HSPA směrem k podpoře efektivnějších paketových služeb. Jak se sítě přesouvaly od primárně hlasových služeb k převládajícímu datovému provozu, který je často přerušovaný, vždy zapnutá povaha řídicího kanálu se stala významnou režií. Před zavedením NT-HS-DPCCH funkce jako Continuous Packet Connectivity (CPC) zavedly DTX/DRX pro jiné kanály, ale HS-DPCCH zůstal trvalým zdrojem režie. NT-HS-DPCCH byl motivován potřebou rozšířit tyto principy šetření baterie a redukce rušení konkrétně na smyčku vysokorychlostní downlinkové řídicí zpětné vazby.

Řeší tyto problémy tím, že dává NodeB kontrolu nad zpětnovazebním kanálem. Síť nyní může aktivovat kanál pouze tehdy, když je to nutné pro naplánované přenosy dat, čímž sladí řídicí signalizaci se skutečnou datovou aktivitou. Tím přímo řeší omezení předchozího přístupu "vždy zapnuto" a umožňuje škálovatelnější a efektivnější HSPA sítě, zejména ve scénářích s mnoha připojenými, ale přerušovaně aktivními uživateli, jako jsou chytré telefony s běžícími aplikacemi na pozadí.

## Klíčové vlastnosti

- Aktivace/deaktivace HS-DPCCH na vyžádání prostřednictvím příkazů NodeB
- Snížení vysílacího výkonu UE v uplinku a spotřeby baterie
- Snížení nárůstu uplinkového rušivého šumu v rámci buňky
- Využívá stávající signalizaci příkazů HS-SCCH pro zpětnou kompatibilitu
- Dynamická koordinace mezi schedulerm NodeB a stavem zpětné vazby UE
- Udržuje plný výkon HSDPA, když je zpětnovazební kanál aktivní

## Související pojmy

- [HS-DPCCH – High Speed Dedicated Physical Control Channel (Uplink)](/mobilnisite/slovnik/hs-dpcch/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [NT-HS-DPCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/nt-hs-dpcch/)
