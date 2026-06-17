---
slug: "ecsn"
url: "/mobilnisite/slovnik/ecsn/"
type: "slovnik"
title: "ECSN – E-AGCH Cyclic Sequence Number"
date: 2025-01-01
abbr: "ECSN"
fullName: "E-AGCH Cyclic Sequence Number"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ecsn/"
summary: "Sekvenční číslo přenášené na kanálu E-AGCH (Enhanced Dedicated Channel Absolute Grant Channel) v síti HSPA. Umožňuje UE detekovat zmeškané nebo nové příkazy absolutního přidělení od sítě, čímž zajišťu"
---

ECSN je sekvenční číslo přenášené na kanálu E-AGCH v síti HSPA, které umožňuje UE detekovat zmeškané nebo nové příkazy absolutního přidělení (absolute grant) pro spolehlivou synchronizaci uplinku.

## Popis

[E-AGCH](/mobilnisite/slovnik/e-agch/) Cyclic Sequence Number (ECSN) je 2bitové pole přenášené jako součást signalizace fyzické vrstvy na kanálu Enhanced Dedicated Channel Absolute Grant Channel (E-AGCH) v sítích 3GPP [HSPA](/mobilnisite/slovnik/hspa/) (High-Speed Packet Access), konkrétně pro Enhanced Uplink ([E-DCH](/mobilnisite/slovnik/e-dch/)). E-AGCH je sdílený downlinkový kanál, který Node B používá k odesílání příkazů absolutního přidělení (Absolute Grant) k uživatelskému zařízení (UE). Tyto příkazy přímo nastavují maximální povolený poměr výkonu, který může UE použít pro svůj přenos na E-DCH, což je klíčový mechanismus pro rychlé plánování uplinku a řízení interference.

ECSN funguje jako modulo-4 čítač. Pokaždé, když Node B odešle novou hodnotu absolutního přidělení konkrétnímu UE (identifikovanému pomocí [E-RNTI](/mobilnisite/slovnik/e-rnti/) na E-AGCH), inkrementuje ECSN. 2bitová hodnota tak cykluje přes 0, 1, 2, 3, 0, 1... ECSN je zakódováno společně s 5bitovou hodnotou absolutního přidělení a 1bitovým indikátorem Signalling of Happy Bit Discount (SHBD) a tvoří tak 8bitovou náplň transportního bloku E-AGCH. Tento blok je následně kanálově zakódován, rozprostřen a přenášen na fyzickém kanálu.

Přijímač UE nepřetržitě monitoruje E-AGCH kvůli příkazům adresovaným jemu. Po úspěšném dekódování příkazu z E-AGCH UE extrahuje ECSN a porovná jej s hodnotou ECSN uloženou z dříve přijatého platného přidělení. Podle specifikace, pokud je nové ECSN větší než staré ECSN (pomocí modulo-4 aritmetiky), UE interpretuje doprovodný příkaz absolutního přidělení jako nový, platný příkaz a musí jej okamžitě aplikovat. Pokud je ECSN rovno uložené hodnotě, UE jej považuje za retransmisi předchozího přidělení a ignoruje jej. Tato jednoduchá logika porovnání je robustní.

Tento mechanismus řeší kritický problém v bezdrátové signalizaci: nespolehlivost fyzického kanálu. Bez ECSN by, pokud by UE zmeškala příkaz absolutního přidělení, pokračovala v provozu se zastaralým přidělením výkonu, což by mohlo způsobit nedostatečné využití nebo nadměrnou interferenci. Naopak, pokud by UE chybně dekódovala šum jako přidělení, mohla by aplikovat nesprávný příkaz. ECSN umožňuje UE detekovat posloupnost. Skok v ECSN indikuje, že byl odeslán nový příkaz, i když předchozí byly ztraceny. Node B, vědom si toho, že UE sleduje ECSN, může být přesvědčen, že nové přidělení bude jako takové rozpoznáno. Tím je zajištěna spolehlivá a deterministická synchronizace stavu plánování uplinku mezi Node B a UE, což je základ pro rychlé, buňkou řízené plánování, které definuje výkon uplinku v HSPA.

## K čemu slouží

ECSN bylo zavedeno za účelem zajištění spolehlivého doručování časově kritických plánovacích příkazů v rámci Enhanced Uplink [HSPA](/mobilnisite/slovnik/hspa/). [E-DCH](/mobilnisite/slovnik/e-dch/) využívá rychlé plánování Node B pro řízení interference v uplinku a maximalizaci propustnosti buňky. Absolutní přidělení (Absolute Grant), odesílané na [E-AGCH](/mobilnisite/slovnik/e-agch/), je nejpřímější a nejmocnější plánovací příkaz, schopný okamžitě změnit maximální vysílací výkon UE. Zmeškaný nebo špatně interpretovaný příkaz přidělení by mohl mít závažné důsledky, jako je vysílání UE na nadměrně vysokém výkonu způsobující kolaps interference, nebo na příliš nízkém výkonu vedoucí k vyhladovění jeho datového toku.

Před zavedením tohoto mechanismu by zajištění spolehlivosti příkazů vyžadovalo potvrzovací protokoly vyšších vrstev, které zavádějí latenci nekompatibilní s 2ms Transmission Time Interval (TTI) plánování HSPA. ECSN poskytuje odlehčené řešení na fyzické vrstvě pro problém detekce sekvence příkazů. Umožňuje UE rozlišit mezi novým příkazem a duplicitním příjmem starého (kvůli retransmisi kanálu nebo špatnému dekódování) a detekovat, kdy pravděpodobně zmeškalo příkaz (pozorováním mezery v sekvenci).

Tento návrh byl motivován potřebou robustnosti i jednoduchosti. Velikost 2 bity je kompromisem, poskytujícím dostatek stavů pro detekci zmeškaných příkazů v krátkém časovém okně bez nadměrné režie. Umožňuje Node B agresivně plánovat uplink s vědomím, že signalizační kanál, i když není zaručen, má vestavěnou metodu pro slaďování stavů. ECSN je klasickým příkladem efektivního návrhu řídicí roviny v bezdrátových systémech, kde je k řešení kritického problému spolehlivosti použita minimální režie, což umožňuje efektivní fungování výkonné datové roviny HSPA.

## Klíčové vlastnosti

- 2bitové modulo-4 cyklické sekvenční číslo přenášené na fyzickém kanálu E-AGCH
- Umožňuje UE detekovat nové, opakované nebo zmeškané příkazy absolutního přidělení (Absolute Grant)
- Inkrementováno Node B pro každou novou hodnotu absolutního přidělení odeslanou UE
- Zpracováváno UE pomocí modulo-4 aritmetiky pro určení platnosti příkazu
- Integrální součást 8bitové náplně transportního bloku E-AGCH
- Poskytuje robustní synchronizaci pro rychlé řízení výkonu a plánování uplinku v HSPA

## Související pojmy

- [E-AGCH – EDCH – Absolute Grant Channel](/mobilnisite/slovnik/e-agch/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)

## Definující specifikace

- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [ECSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecsn/)
