---
slug: "scl"
url: "/mobilnisite/slovnik/scl/"
type: "slovnik"
title: "SCL – Supported Codec List"
date: 2025-01-01
abbr: "SCL"
fullName: "Supported Codec List"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/scl/"
summary: "Seznam audio a video kodeků podporovaných UE, který se vyměňuje při navazování hovoru, aby umožnil řízení transkódéru mimo přenosovou cestu (OoBTC). Zajišťuje, že síť a koncové zařízení mohou vyjednat"
---

SCL je seznam audio a video kodeků podporovaných uživatelským zařízením, který se vyměňuje během navazování hovoru, aby umožnil vyjednání a výběr kodeku pro lepší kvalitu hlasu a snížení zpoždění.

## Popis

Seznam podporovaných kodeků (SCL) je klíčový informační prvek používaný v sítích 3GPP, konkrétně definovaný v kontextu řízení transkódéru mimo přenosovou cestu (OoBTC). Jedná se o strukturovaný seznam, typně přenášený v rámci protokolů pro řízení relace, jako je [SIP](/mobilnisite/slovnik/sip/), nebo v konkrétních zprávách 3GPP [NAS](/mobilnisite/slovnik/nas/)/[RRC](/mobilnisite/slovnik/rrc/), který vyjmenovává všechny řečové a multimediální kodeky, které je uživatelské zařízení (UE) schopno kódovat a dekódovat. Tento seznam zahrnuje identifikátory kodeků a jejich přidružené konfigurační parametry, jako jsou přenosové rychlosti, velikosti rámců a další provozní režimy. Primární technickou funkcí SCL je umožnit vyjednání kodeku od konce ke konci před navázáním hovoru nebo relace.

Při zahájení relace volající UE zahrne svůj SCL do žádosti o navázání relace. Tato žádost prochází jádrem sítě, případně zahrnuje [MSC](/mobilnisite/slovnik/msc/) Server, [MGW](/mobilnisite/slovnik/mgw/) nebo IMS entity. Síť SCL prozkoumá a porovná jej s možnostmi volaného UE, které také poskytuje svůj vlastní SCL. Na základě politiky operátora, možností sítě a průniku obou SCL sít vybere optimální kodek pro relaci. Tento výběr je následně sdělen zpět oběma UE prostřednictvím potvrzovací zprávy, čímž je zajištěno, že obě strany používají stejný kodek od začátku toku médií.

Architektura pro využití SCL je integrována do vrstev řízení hovoru a správy relací. V doménách s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) interaguje s procedurami provozu bez transkódéru (TrFO). V IP multimediální podsystému (IMS) je přenášen v rámci výměn nabídky a odpovědi SIP/[SDP](/mobilnisite/slovnik/sdp/). SCL umožňuje síti obejít mezilehlé transkódovací jednotky (Traffic Bearer Transcoder, TTB), pokud je společný kodek podporován od konce ke konci, a tak navázat hovor bez transkódéru (TrFO) nebo vysokokvalitní hlasový hovor založený na IMS. Tato přímá přenosová cesta je klíčová pro zachování kvality hlasu, protože každý krok transkódování může způsobit zkreslení a zpoždění. Správa a zpracování SCL jsou proto klíčové pro implementaci efektivního OoBTC, což je základní funkce pro moderní služby vysokokvalitního hlasu, jako jsou VoLTE a VoNR.

## K čemu slouží

SCL byl vytvořen, aby vyřešil klasický problém telekomunikací – neshodu kodeků a povinné transkódování v přenosové cestě. V raných mobilních sítích hlasové hovory často zahrnovaly více převodů kodeků, protože volající telefon, síťové vybavení a volaný telefon mohly podporovat různé kodeky. Pro rádiový přístup byl často používán pevný výchozí kodek (jako [AMR-NB](/mobilnisite/slovnik/amr-nb/)), ale jádrová síť jej pro propojení transkódovala do jiného formátu (jako G.711). Každá operace transkódování zhoršuje kvalitu zvuku, přidává latenci a spotřebovává další výpočetní prostředky v síťových uzlech, jako je Media Gateway (MGW).

Motivací pro SCL a OoBTC bylo přesunout tento proces vyjednávání a výběru kodeku 'mimo přenosovou cestu' – tedy provést jej v řídicí rovině před nastavením přenosové cesty médií. To umožňuje síti zjistit, zda oba koncové body podporují společný kodek. Pokud ano, síť může mezi nimi nakonfigurovat přímý přenosový kanál bez transkódéru, což dramaticky zlepšuje vnímanou kvalitu hlasu a snižuje zpoždění mezi ústy a uchem. Toto byl významný krok k službám vysokokvalitního hlasu. Zavedení SCL v Rel-8 bylo v souladu s širším úsilím o sítě plně založené na IP a IMS, kde IP konektivita od konce ke konci učinila provoz bez transkódéru dosažitelnějším cílem, což přímo řešilo kvalitativní omezení staršího provozu bez tandemového kódování (TFO), který byl řešením v přenosové cestě.

## Klíčové vlastnosti

- Vyjmenovává audio a video kodeky podporované UE včetně parametrů
- Vyměňuje se v řídicí rovině během navazování relace (např. přes SIP/SDP)
- Umožňuje síti řízený výběr optimálního kodeku
- Základní prvek pro umožnění provozu bez transkódéru (TrFO)
- Snižuje celkové zpoždění od konce ke konci tím, že se vyhne mezilehlému transkódování
- Zlepšuje kvalitu hlasu tím, že zachovává původní stream kodeku

## Související pojmy

- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)

## Definující specifikace

- **TR 43.903** (Rel-19) — Feasibility Study for A-interface over IP

---

📖 **Anglický originál a plná specifikace:** [SCL na 3GPP Explorer](https://3gpp-explorer.com/glossary/scl/)
