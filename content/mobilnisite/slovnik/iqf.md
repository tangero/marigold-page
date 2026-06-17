---
slug: "iqf"
url: "/mobilnisite/slovnik/iqf/"
type: "slovnik"
title: "IQF – Identity Query Function"
date: 2025-01-01
abbr: "IQF"
fullName: "Identity Query Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iqf/"
summary: "Funkce pro dotaz na identitu (IQF) je síťová funkce 5G, která poskytuje službu ověření identity s ochranou soukromí. Umožňuje konzumní síťové funkci (NF) dotazovat se, zda zakrytý identifikátor účastn"
---

IQF je síťová funkce 5G, která poskytuje ověření identity s ochranou soukromí tím, že umožňuje ostatním funkcím dotazovat se, zda zakrytý identifikátor účastníka odpovídá platnému předplatnému.

## Popis

Funkce pro dotaz na identitu (IQF) je bezpečnostní funkce zavedená ve specifikaci 3GPP Release 16 jako součást vylepšené bezpečnostní architektury 5G. Působí v domácí veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)) a slouží jako klíčová ochrana soukromí. Jejím hlavním úkolem je zpracovávat dotazy týkající se zakrytých identit uživatelů. V 5G se za účelem ochrany soukromí uživatele nikdy nepřenáší trvalý identifikátor účastníka (SUPI) přes rozhraní v nezašifrované podobě. Namísto toho UE odesílá zakrytý identifikátor účastníka (SUCI), což je zašifrovaná forma SUPI. IQF poskytuje způsob, jak mohou ostatní autorizované síťové funkce tento SUCI ověřit, aniž by se tyto funkce dostaly k SUPI v prostém textu.

Architektonicky je IQF samostatná síťová funkce ([NF](/mobilnisite/slovnik/nf/)), která vystavuje rozhraní založené na službách, typicky založené na [HTTP](/mobilnisite/slovnik/http/)/2. Primárně komunikuje s funkcí Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) a funkcí Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)). Když konzumní NF (jako například Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo Service Communication Proxy (SCP)) obdrží žádost o službu obsahující SUCI, může potřebovat před dalším postupem ověřit stav předplatného uživatele. Namísto aby SUCI dešifrovala sama (což by vyžadovalo privátní klíč domácí sítě), odešle konzumní NF dotaz na identitu do IQF. Tento požadavek obsahuje SUCI a kontext dotazu.

IQF tento požadavek zpracuje tak, že nejprve dešifruje SUCI, aby získala SUPI. Tato dešifrace je provedena bezpečně v důvěryhodném prostředí IQF pomocí privátního klíče domácí sítě. IQF následně provede vyhledání v UDM, aby ověřila stav předplatného spojený s tímto SUPI. Zásadní je, že IQF nevrací SUPI dotazující se NF. Namísto toho vrátí binární odpověď (např. platný/neplatný) nebo token potvrzující platnost předplatného. Tento proces zajišťuje, že konzumní NF může autorizovat žádost o službu na základě platné identity, zatímco je zachován princip důvěrnosti identity účastníka. SUPI zůstává známé pouze UE, AUSF (během ověřování) a UDM/IQF v rámci domácí sítě.

## K čemu slouží

IQF byla vytvořena za účelem vyřešení napětí mezi autorizací služeb a soukromím uživatele v sítích 5G. 5G zavedlo silnou ochranu soukromí identity účastníka povinným používáním SUCI přes rádiové rozhraní. Mnoho síťových služeb a expozičních [API](/mobilnisite/slovnik/api/) však potřebuje znát stav předplatného uživatele, aby mohlo autorizovat požadavky. Před zavedením IQF musely síťové funkce, které potřebovaly uživatele ověřit, buď SUCI zpracovávat samy (což narušovalo hranici soukromí), nebo se spoléhat na nepřímé metody, které byly neefektivní nebo nezabezpečené. Například aplikační server třetí strany přistupující k síti přes [NEF](/mobilnisite/slovnik/nef/) mohl obdržet SUCI a potřebovat zkontrolovat, zda je uživatel platným zákazníkem.

IQF poskytuje standardizované, bezpečné a soukromí chránící řešení tohoto problému. Stanovuje jasné funkční oddělení: IQF je jedinou entitou (kromě AUSF během primárního ověřování), která v jádru sítě dešifruje SUCI. Tím se centralizuje zpracování citlivého privátního klíče a minimalizuje se prostor pro útok. Umožňuje nové obchodní modely a scénáře síťové expozice, kde externí nebo interní poskytovatelé služeb mohou ověřit legitimitu uživatele, aniž by se dozvěděli jeho trvalou identitu, čímž jsou dodrženy přísné požadavky na soukromí podle GDPR a podobných předpisů. IQF je klíčovým prvkem umožňujícím bezpečné operace architektury založené na službách (SBA) ve scénářích využívajících zakryté identifikátory.

## Klíčové vlastnosti

- Poskytuje ověření zakrytých identifikátorů účastníka (SUCI) s ochranou soukromí bez vystavení SUPI.
- Působí jako centralizovaná, důvěryhodná funkce pro dešifrování SUCI pomocí privátního klíče domácí sítě.
- Vystavuje rozhraní založené na službách (např. Niqf) pro využití ostatními autorizovanými síťovými funkcemi.
- Vrací dotazujícím se entitám potvrzovací tokeny nebo binární odpovědi o platnosti.
- Umožňuje autorizaci služeb pro aplikace třetích stran a interní NF při zachování důvěrnosti identity účastníka.
- Integruje se s UDM za účelem ověření stavu předplatného odpovídajícího dešifrovanému SUPI.

## Související pojmy

- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [IQF na 3GPP Explorer](https://3gpp-explorer.com/glossary/iqf/)
