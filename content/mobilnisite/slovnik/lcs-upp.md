---
slug: "lcs-upp"
url: "/mobilnisite/slovnik/lcs-upp/"
type: "slovnik"
title: "LCS-UPP – Location Services User Plane Protocol"
date: 2025-01-01
abbr: "LCS-UPP"
fullName: "Location Services User Plane Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lcs-upp/"
summary: "Location Services User Plane Protocol (LCS-UPP) je aplikační protokol fungující nad LCS uživatelskou rovinou (LCS-UP). Definuje formát a postupy výměny polohovacích datových paketů (PDU) obsahujících"
---

LCS-UPP je aplikační protokol pro výměnu paketů s polohovacími daty, jako jsou měření a výsledky lokalizace, mezi uživatelským zařízením a serverem pro určování polohy přes 5G uživatelskou rovinu.

## Popis

Location Services User Plane Protocol (LCS-UPP) je konkrétní protokol realizující rámec [LCS](/mobilnisite/slovnik/lcs/) uživatelské roviny ([LCS-UP](/mobilnisite/slovnik/lcs-up/)). Je to aplikační protokol fungující nad standardním 5G transportním zá zásobníkem uživatelské roviny (IP, [UDP](/mobilnisite/slovnik/udp/), [GTP-U](/mobilnisite/slovnik/gtp-u/)). LCS-UPP definuje strukturu Protocol Data Units ([PDU](/mobilnisite/slovnik/pdu/)), které přenášejí veškeré polohovací informace vyměňované přímo přes datový kanál, což umožňuje efektivní přenosy velkých objemů dat, které by byly neúnosné pro signalizaci přes řídicí rovinu.

Technicky LCS-UPP PDU zapouzdřují datové části protokolů vyšších vrstev pro určování polohy. Nejvýznamnějším z nich je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)), který je přizpůsoben pro 5G. V kontextu LCS-UP se zprávy LPP (obsahující žádosti o měření, hlášení měření, doručování asistenčních dat a informace o poloze) neposílají přes [NAS](/mobilnisite/slovnik/nas/), ale místo toho jsou zabaleny jako datová část v rámci LCS-UPP PDU. Vrstva LCS-UPP přidává vlastní hlavičku obsahující řídicí informace, jako je typ PDU (např. Data, Acknowledge), pořadové číslo pro spolehlivé doručení (je-li třeba) a identifikátory pro přiřazení PDU ke konkrétní polohovací relaci nebo transakci. Toto zapouzdřené LPP-v-LCS-UPP PDU je následně odesláno přes zavedený bearer uživatelské roviny PDU Session.

Protokol funguje mezi dvěma hlavními koncovými body: vrstvou LCS-UPP v UE a vrstvou LCS-UPP v Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)). gNB a UPF jsou pro obsah LCS-UPP transparentní; pouze přeposílají IP pakety obsahující GTP-U zapouzdřená LCS-UPP PDU. LCS-UPP podporuje jak režim s navázáním spojení, tak režim bez spojení. Pro trvalou polohovací relaci s častou výměnou dat (např. kontinuální sledování) lze navázat kontext s navázáním spojení, který spravuje pořadová čísla a potvrzení. Pro jednorázové doručení asistenčních dat lze použít jednoduchý datagram bez spojení. Protokol je navržen jako odlehčený, s minimalizací režie, aby byla zachována výhoda nízkého zpoždění uživatelské roviny. Funguje ve spolupráci s protokoly řídicí roviny (jako je LPP přes NAS), které se stále používají pro navazování relací, vyjednávání schopností a aktivaci/deaktivaci přenosu polohovacích dat přes uživatelskou rovinu.

## K čemu slouží

LCS-UPP byl vyvinut, aby poskytl standardizovaný a efektivní mechanismus zapouzdření a doručování dat polohovacích protokolů přes 5G uživatelskou rovinu. Před jeho zavedením se polohovací protokoly, jako je LPP, přenášely výhradně přes řídicí rovinu (NAS), která nebyla navržena pro datovou náročnost pokročilého určování polohy. Potřeba protokolu pro uživatelskou rovinu se stala zjevnou s příchodem případů užití 5G-Advanced, které vyžadovaly přenos velkých souborů asistenčních dat (např. korekcí real-time kinematic (RTK), dat pro precise point positioning (PPP)) a vysokofrekvenčních proudů nezpracovaných senzorických měření z UE.

Protokol řeší problém, jak spolehlivě a efektivně přenášet strukturované polohovací zprávy v rámci nestrukturovaného toku IP paketů uživatelské roviny. Poskytuje potřebný management relací, rámování zpráv a volitelné mechanismy spolehlivosti na aplikační vrstvě bez nutnosti spoléhat se na TCP, které by mohlo přinést nepřijatelné zpoždění a kolísání. Definováním LCS-UPP vytvořila 3GPP účelový kanál, který umožňuje využití bohatých funkcí LPP (a budoucích polohovacích protokolů) v kontextu vysoce výkonné datové roviny. To umožňuje síťovým operátorům a poskytovatelům služeb nabízet diferencované služby určování polohy s vysokou přesností (positioning-as-a-service) se zaručenou QoS, což je klíčový prvek pro monetizaci schopností 5G sítí ve vertikálních trzích.

## Klíčové vlastnosti

- Zapouzdřovací protokol pro přenos LPP a dalších zpráv polohovacích protokolů přes uživatelskou rovinu
- Definuje LCS-UPP PDU s hlavičkami pro správu relací a transakcí
- Podporuje jak potvrzovaný (spolehlivý), tak nepotvrzovaný (best-effort) režim přenosu dat
- Umožňuje efektivní přenos velkých souborů asistenčních dat a častých hlášení měření
- Funguje transparentně přes standardní GTP-U tunely 5G UPF-gNB
- Navržen pro nízké zpoždění a minimální režii protokolu

## Související pojmy

- [LCS-UP – Location Services User Plane](/mobilnisite/slovnik/lcs-up/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.572** (Rel-19) — 5G LCS User Plane Protocol Specification
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [LCS-UPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcs-upp/)
