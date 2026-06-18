---
slug: "cda"
url: "/mobilnisite/slovnik/cda/"
type: "slovnik"
title: "CDA – Capacity Deallocation Acknowledgement"
date: 2025-01-01
abbr: "CDA"
fullName: "Capacity Deallocation Acknowledgement"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cda/"
summary: "Signalizační zpráva v UMTS, která potvrzuje úspěšné uvolnění rádiových zdrojů. Je součástí procedur řízení kapacity protokolu řízení rádiového spoje (RLC) a zajišťuje efektivní využití rozhraní vzduch"
---

CDA je signalizační zpráva řízení rádiového spoje (RLC) v UMTS, která potvrzuje úspěšné uvolnění rádiových zdrojů za účelem zajištění efektivního řízení kapacity rozhraní vzduchu.

## Popis

Capacity Deallocation Acknowledgement (CDA) je specifická řídicí zpráva na vrstvě protokolu řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) standardizovaná v 3GPP UMTS. Vrstva RLC, pracující v potvrzovaném režimu ([AM](/mobilnisite/slovnik/am/)), je zodpovědná za spolehlivý přenos dat, segmentaci, zpětné složení a doručování ve správném pořadí. Její kritickou doplňkovou funkcí je dynamické řízení kapacity transportního kanálu přidělené rádiovému přenosovému okruhu (Radio Bearer). Tato kapacita, často definovaná kombinacemi transportních formátů (TFCs), je řízena prostřednictvím procedur přidělení kapacity ([CA](/mobilnisite/slovnik/ca/)) a uvolnění kapacity ([CD](/mobilnisite/slovnik/cd/)). Zpráva CDA je explicitní kladné potvrzení odeslané uživatelským zařízením (UE) v odpovědi na příkaz k uvolnění kapacity (CD) přijatý od [UTRAN](/mobilnisite/slovnik/utran/) (UMTS Terrestrial Radio Access Network).

Z architektonického hlediska se procedury účastní entity RLC jak v UE, tak v řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). Když síť rozhodne, že je nutné snížit přidělenou kapacitu transportního kanálu pro konkrétní rádiový přenosový okruh – například kvůli poklesu datového provozu nebo pro vyrovnání zatížení sítě – odešle příkaz k uvolnění kapacity prostřednictvím řídicí [PDU](/mobilnisite/slovnik/pdu/) RLC na downlinku. Tento příkaz pokynuje UE, aby uvolnilo určenou část své aktuálně přidělené uplinkové kapacity. Po přijetí a úspěšném zpracování tohoto příkazu CD musí entita RLC v UE akci potvrdit, aby obě strany měly konzistentní pohled na dostupné zdroje. UE sestaví a odešle zpět do UTRAN zprávu CDA jako řídicí PDU RLC na uplinku.

Samotná zpráva CDA obsahuje specifické informační prvky, které ji spojují s původním příkazem k uvolnění, a zajišťují tak spolehlivé přiřazení. Tento mechanismus potvrzení je klíčový pro prevenci nesouladu ve stavu zdrojů mezi UE a sítí, který by mohl vést k chybám přenosu nebo neefektivnímu využití kapacity. Bez kladného potvrzení, jako je CDA, by síť mohla předpokládat selhání uvolnění a udržovat nesprávný, nafouknutý pohled na přidělené zdroje UE, nebo by mohla předčasně zkusit nové přidělení na kapacitu, o které se domnívá, že je volná. CDA tedy finalizuje transakci uvolnění kapacity, což umožňuje bezpečné přerozdělení uvolněných zdrojů (např. specifických kombinací transportních formátů) jiným uživatelům nebo službám, a přímo tak přispívá k celkové spektrální efektivitě a stabilitě rádiového rozhraní UMTS.

## K čemu slouží

CDA byla vytvořena pro uspokojení potřeby spolehlivé a explicitní signalizace v dynamických procedurách řízení kapacity v potvrzovaném režimu ([AM](/mobilnisite/slovnik/am/)) RLC v UMTS. V sdíleném, paketově orientovaném rádiovém prostředí jsou zdroje vzácné a musí být přidělovány a uvolňovány rychle v reakci na kolísající poptávku uživatelů. Starší jednodušší systémy nebo nepotvrzované procedury riskovaly úniky zdrojů nebo konflikty, kdy měl vysílač a přijímač odlišné představy o dostupné kapacitě. To mohlo způsobit ztrátu dat, zastavení protokolu nebo neoptimální propustnost sítě.

Zavedení explicitního potvrzení pro příkazy k uvolnění kapacity jako součást specifikací UMTS R99 poskytlo robustní mechanizmus handshake. Vyřešilo problém zajištění synchronizace stavu mezi UE a UTRAN pro zdroje transportních kanálů. To bylo obzvláště důležité pro služby vyžadující spolehlivé doručování dat, jako jsou interaktivní a na pozadí běžící třídy provozu, kde RLC pracuje v potvrzovaném režimu. Procedura CDA společně s potvrzením přidělení kapacity (CAA) vytvořila úplný a spolehlivý dialog řízení kapacity, což síti umožnilo agresivnější a efektivnější strategie řízení rádiových zdrojů při zachování integrity protokolu a kvality služeb.

## Klíčové vlastnosti

- Explicitní potvrzení příkazů k uvolnění kapacity
- Součást řídicího protokolu potvrzovaného režimu (AM) RLC
- Zajišťuje synchronizaci stavu mezi UE a UTRAN
- Předchází únikům zdrojů a konfliktům v přidělování
- Přenášena uvnitř řídicích protokolových datových jednotek (PDU) RLC
- Umožňuje efektivní a dynamické řízení rádiových zdrojů

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding

---

📖 **Anglický originál a plná specifikace:** [CDA na 3GPP Explorer](https://3gpp-explorer.com/glossary/cda/)
