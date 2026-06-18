---
slug: "oa"
url: "/mobilnisite/slovnik/oa/"
type: "slovnik"
title: "OA – Outgoing Access (CUG SS)"
date: 2025-01-01
abbr: "OA"
fullName: "Outgoing Access (CUG SS)"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oa/"
summary: "Funkce doplňkové služby v rámci Skupiny uzavřených účastníků (CUG), která řídí schopnost uživatele uskutečňovat odchozí hovory na čísla mimo jeho určenou skupinu. Je klíčovou součástí pro implementaci"
---

OA je funkce doplňkové služby Skupiny uzavřených účastníků (CUG SS), která řídí schopnost uživatele uskutečňovat odchozí hovory na čísla mimo jeho určenou privátní skupinu.

## Popis

Outgoing Access (OA) je specifická schopnost v rámci doplňkové služby Skupiny uzavřených účastníků ([CUG](/mobilnisite/slovnik/cug/) [SS](/mobilnisite/slovnik/ss/)) definované standardy 3GPP. Skupina uzavřených účastníků je služba, ve které může definovaná skupina účastníků komunikovat mezi sebou, typicky s omezeními pro hovory na veřejnou síť a z ní. Funkce OA konkrétně stanovuje oprávnění pro člena CUG iniciovat hovory na cíle mimo jeho vlastní CUG. Síť rozhoduje, zda je pokus o odchozí hovor povolen, na základě předplatitelských dat CUG účastníka, která zahrnují indikátor 'Outgoing Access'. Tato data jsou uložena v domácím registračním centru ([HLR](/mobilnisite/slovnik/hlr/)) nebo na domácím předplatitelském serveru ([HSS](/mobilnisite/slovnik/hss/)) a jsou poskytnuta obsluhujícímu ústřednímu přepojovacímu centru ([MSC](/mobilnisite/slovnik/msc/)) nebo funkci řízení relací během registrace a sestavování hovoru.

Když se předplatitel CUG s povolenou funkcí OA pokusí uskutečnit hovor, obsluhující síťový uzel (např. MSC) provede kontrolu CUG. Zkontroluje volané číslo vůči seznamu členství předplatitele v CUG. Pokud volané číslo není členem žádné z CUG předplatitele, je vyhodnocen indikátor OA. Pokud je OA povolena ('OA allowed'), hovor pokračuje jako běžný hovor do veřejné sítě nebo do jiné CUG (pokud je komunikace mezi CUG povolena). Pokud OA povolena není ('OA not allowed'), pokus o hovor je síťovou odmítnut. Toto vynucování je základní součástí logiky řízení hovorů v jádrové síti s přepojováním okruhů nebo v IMS jádru.

Funkce OA funguje v kombinaci s dalšími funkcemi CUG, jako je Incoming Access ([IA](/mobilnisite/slovnik/ia/)), která řídí schopnost přijímat hovory zvenčí CUG. Kombinace nastavení OA a IA definuje komunikační profil pro člena CUG, například 'plně uzavřený' (žádné příchozí ani odchozí externí hovory) nebo 'hybridní' (odchozí povoleny, ale příchozí blokovány, nebo naopak). Tato služba je klíčová pro podniková řešení a řešení pro vertikální trhy, umožňujíc organizacím vytvářet bezpečné, nákladově kontrolované telefonní skupiny v rámci infrastruktury veřejné mobilní sítě. Její implementace závisí na standardizovaném signalizačním protokolu mezi síťovými prvky pro přenos informací CUG a výsledků autorizace.

## K čemu slouží

Funkce Outgoing Access byla vytvořena, aby poskytla detailní kontrolu nad komunikací v rámci služeb Skupin uzavřených účastníků, což je základní požadavek pro podnikové a privátní síťové nabídky. Před standardizovanými službami [CUG](/mobilnisite/slovnik/cug/) operátoři nabízeli základní funkce skupinového volání s omezenou flexibilitou, často vyžadující složité a proprietární konfigurace ústředen. Specifikace OA vyřešila problém nekontrolovaných komunikačních nákladů a bezpečnosti tím, že umožnila poskytovatelům služeb explicitně definovat, zda členové skupiny mohou volat mimo privátní skupinu.

Tato schopnost řeší několik klíčových potřeb: správu nákladů pro podniky (prevence neautorizovaných drahých hovorů), bezpečnost pro citlivé organizace (omezení komunikačních kanálů) a diferenciaci služeb pro operátory. Standardizací OA jako součásti CUG [SS](/mobilnisite/slovnik/ss/) v 3GPP Release 4 byla zajištěna interoperabilita mezi různými síťovými dodavateli a operátory, což umožnilo bezproblémové národní a mezinárodní služby CUG. Funkce umožňuje vytváření různých úrovní služeb, od zcela izolovaných skupin až po skupiny s řízeným externím přístupem, a splňuje tak různé požadavky zákazníků bez nutnosti nestandardních síťových implementací.

## Klíčové vlastnosti

- Řídí oprávnění členů CUG iniciovat hovory na čísla mimo jejich předplacenou CUG(y).
- Definována indikátorem 'OA allowed' nebo 'OA not allowed' v předplatitelských datech CUG účastníka.
- Vynucována MSC nebo funkcí řízení hovorů během sestavování hovoru na základě dat z HLR/HSS.
- Funguje v kombinaci s Incoming Access (IA) k definování komplexních komunikačních profilů CUG.
- Podporuje více hodnot indexu CUG pro předplatitele patřící do více než jedné skupiny.
- Využívá standardizovanou signalizaci MAP (Mobile Application Part) nebo Diameter pro přenos informací CUG.

## Definující specifikace

- **TR 21.866** (Rel-15) — Study on Energy Efficiency in 3GPP Standards
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.085** (Rel-19) — Closed User Group (CUG) Supplementary Service Stage 2
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.454** (Rel-8) — Closed User Group (CUG) Protocol Specification
- **TS 24.654** (Rel-19) — Closed User Group (CUG) supplementary service

---

📖 **Anglický originál a plná specifikace:** [OA na 3GPP Explorer](https://3gpp-explorer.com/glossary/oa/)
