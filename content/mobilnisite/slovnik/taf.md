---
slug: "taf"
url: "/mobilnisite/slovnik/taf/"
type: "slovnik"
title: "TAF – Terminal Adaptation Function"
date: 2025-01-01
abbr: "TAF"
fullName: "Terminal Adaptation Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/taf/"
summary: "Terminal Adaptation Function (TAF) je funkční entita v zastaralých jádrech sítí 3GPP s přepojováním okruhů, konkrétně pro GSM a rané UMTS. Adaptuje datové koncové zařízení (DTE), jako je počítač, na m"
---

TAF je funkční entita v zastaralých sítích GSM a UMTS, která adaptuje datové koncové zařízení na mobilní ukončovací zařízení tím, že zajišťuje převod protokolů a adaptaci přenosové rychlosti pro služby přepojování okruhů.

## Popis

Terminal Adaptation Function (TAF) je vrstva pro adaptaci protokolů definovaná v raných specifikacích 3GPP, primárně pro GSM a doménu přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)) v UMTS. Logicky sídlí ve uživatelském zařízení (UE), ale je často konceptualizována jako funkce umístěná mezi datovým koncovým zařízením ([DTE](/mobilnisite/slovnik/dte/)) a mobilním ukončením ([MT](/mobilnisite/slovnik/mt/)). DTE je koncové uživatelské zařízení, které generuje nebo spotřebovává data (např. notebook, [PDA](/mobilnisite/slovnik/pda/) nebo fax), zatímco MT je zařízení pro přístup do mobilní sítě (např. GSM telefon, [PCMCIA](/mobilnisite/slovnik/pcmcia/) karta nebo vestavěný modul), které zajišťuje rádiovou komunikaci. Primární úlohou TAF je odstranit nekompatibilitu mezi datovými protokoly a rozhraními používanými DTE (typicky standardní sériová rozhraní jako V.24/V.28 nebo [USB](/mobilnisite/slovnik/usb/)) a specifickými protokoly vyžadovanými pro přenos dat přes doménu CS mobilní sítě.

Provozně TAF provádí dva klíčové typy adaptace: převod protokolů a adaptaci přenosové rychlosti. Při převodu protokolů TAF překládá mezi řídicí signalizací používanou DTE (např. sada příkazů AT dle [ITU-T](/mobilnisite/slovnik/itu-t/) V.25ter) a interní signalizací MT a sítě. Pro adaptaci přenosové rychlosti přizpůsobuje datový tok DTE dostupným přenosovým rychlostem nosičů v mobilní síti. V GSM jsou nosiče pro přepojování okruhů definovány s konkrétními rychlostmi (např. 9,6 kbps, 14,4 kbps). DTE může pracovat s jinou rychlostí (např. sériový port na 115,2 kbps). TAF používá standardní schémata adaptace rychlosti definovaná v řadě ITU-T V, jako je V.110 nebo efektivnější V.120, aby zabalila uživatelská data do strukturovaných rámců vhodných pro mobilní nosič. To zahrnuje bitové doplňování, synchronizaci a správu řídicích signálů v pásmu.

Architektonicky je TAF specifikována v 3GPP TS 27.001 a souvisejících specifikacích (historicky v řadách 04.xx a 07.xx). Definuje servisní primitiva a logický tok informací mezi DTE a MT. Ve fyzické implementaci může být TAF software ve firmwaru modemu telefonu při připojení přes sériový kabel, nebo může být součástí softwaru ovladače v počítači používajícím mobilní datovou kartu. TAF komunikuje s dalšími vrstvami protokolů v MT, jako je Radio Link Protocol ([RLP](/mobilnisite/slovnik/rlp/)) pro opravu chyb a podkladová fyzická vrstva. Její existence byla klíčová pro umožnění široké škály koncových zařízení přistupovat k mobilním datovým službám před tím, než všudypřítomnost integrovaných, nativně IP smartphonů a jader s přepojováním paketů učinila takovou explicitní adaptaci méně viditelnou.

## K čemu slouží

Terminal Adaptation Function byla vytvořena k vyřešení problému připojení obecných datových zařízení k raným digitálním celulárním sítím, které byly primárně navrženy pro hlas. V 90. letech 20. století se vize mobilních sítí rozšířila o datové služby jako fax, vytáčený internet a transakce v místě prodeje. Stávající ekosystém datových terminálů (počítače, faxové přístroje) však používal dobře zavedená rozhraní a protokoly pro drátovou telekomunikaci (např. RS-232, standardy řady V). Na druhé straně rádiové rozhraní a jádro mobilní sítě používaly zcela odlišné protokoly optimalizované pro bezdrátový přenos a telefonii s přepojováním okruhů.

TAF tuto mezeru překlenula poskytnutím standardizované adaptační vrstvy. Její vznik byl motivován potřebou interoperability a růstu trhu; bez ní by každá kombinace DTE a MT vyžadovala proprietární řešení, což by bránilo adopci. TAF standardizovala způsob, jakým počítač "vidí" mobilní telefon jako modem (pomocí příkazů AT), a jak je datový tok formátován pro síť. Vyřešila tak omezení dřívějších, více ad-hoc přístupů k mobilním datům. Historicky se specifikace TAF vyvinuly ze standardů GSM (Release 4 a starší) do UMTS, podporující vyšší přenosové rychlosti a efektivnější adaptační protokoly jako V.120. Zatímco její význam poklesl s ukončováním služeb přepojování okruhů a nástupem neustále připojených, IP-bazovaných paketových dat (GPRS, EDGE, HSPA, LTE, NR), kde je terminál sám IP-schopný, byla TAF základním prvkem umožňujícím první generaci mobilních datových služeb, spojujícím svět tradičních datových komunikací a mobilní telefonie.

## Klíčové vlastnosti

- Převod protokolů mezi řídicími signály DTE (příkazy AT) a signalizací MT/interní sítě
- Adaptace přenosové rychlosti mezi rychlostmi rozhraní DTE a přenosovými rychlostmi nosičů mobilní sítě (např. pomocí V.110, V.120)
- Logická funkce sídlící mezi datovým koncovým zařízením (DTE) a mobilním ukončením (MT)
- Nezbytná pro umožnění služeb přepojování okruhů a faxu přes GSM/UMTS
- Standardizována v 3GPP TS 27.001 a souvisejících specifikacích
- Podporuje různá fyzická rozhraní (např. sériové V.24, USB)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 46.002** (Rel-19) — Introduction to GSM Half-Rate Speech Processing
- **TS 46.041** (Rel-19) — GSM Half Rate Speech DTX Operation
- **TS 46.051** (Rel-19) — GSM Enhanced Full Rate Speech Processing Intro

---

📖 **Anglický originál a plná specifikace:** [TAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/taf/)
