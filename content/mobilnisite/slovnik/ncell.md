---
slug: "ncell"
url: "/mobilnisite/slovnik/ncell/"
type: "slovnik"
title: "NCELL – Neighbouring (of current serving) Cell"
date: 2025-01-01
abbr: "NCELL"
fullName: "Neighbouring (of current serving) Cell"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ncell/"
summary: "Jakákoli buňka, která je geograficky sousední nebo v rádiové blízkosti aktuální obslužné buňky UE. Síť a UE nepřetržitě monitorují NCELLy, aby se připravily na potenciální předání spojení, což zajišťu"
---

NCELL je geograficky sousední nebo rádiově blízká buňka vůči aktuální obslužné buňce uživatele, která je monitorována pro přípravu na potenciální předání spojení (handover) a udržení kontinuity služby.

## Popis

Sousední buňka (NCELL) je základním provozním konceptem ve všech celulárních sítích od GSM až po 5G NR. Odkazuje na jakoukoli buňku, potenciálně patřící ke stejné nebo jiné základnové stanici (gNB, [eNB](/mobilnisite/slovnik/enb/), NodeB, [BTS](/mobilnisite/slovnik/bts/)) a případně i jiné frekvenční vrstvě nebo technologii rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)), která je kandidátem pro připojení uživatelského zařízení (UE), když toto opustí pokrytí své aktuální obslužné buňky. Správa NCELLů je klíčovou funkcí subsystémů správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) a správy mobility ([MM](/mobilnisite/slovnik/mm/)). Základnová stanice obslužné buňky udržuje Tabulku sousedních vztahů ([NRT](/mobilnisite/slovnik/nrt/)), což je databáze známých NCELLů, jejich identifikátorů (jako [PCI](/mobilnisite/slovnik/pci/)/[ECGI](/mobilnisite/slovnik/ecgi/)/CGI), kmitočtů nosných a dalších relevantních parametrů.

Proces funguje prostřednictvím nepřetržitého měření a hlášení. Síť nakonfiguruje UE měřicí konfigurací pomocí signalizace RRC. Tato konfigurace specifikuje, které NCELLy (podle kmitočtu a identifikátoru buňky) měřit, jaké měřicí události hlásit (např. Událost A3: soused se stane o offset lepší než obslužná) a kritéria pro hlášení. UE následně provádí měření na obslužné buňce a uvedených NCELLech, typicky na referenčních signálech jako SSB v NR nebo CRS v LTE. Když je spuštěna měřicí událost (např. kvalita signálu NCELLu překročí kvalitu obslužné buňky plus hysterezní okraj), UE odešle měřicí hlášení síti. RRM algoritmus sítě se pak rozhodne, zda provést předání spojení (handover) na tento NCELL. Koncept NCELL je technologicky neutrální; platí pro scénáře mobility v rámci kmitočtu, mezi kmitočty a mezi různými RAT (např. NR na LTE).

Kromě předání spojení se informace o NCELLech používají pro další funkce RRM. V režimu idle/inactive používá UE měření NCELLů pro převýběr buňky, řízený vysílanými systémovými informacemi, které poskytují seznam sousedních buněk (NCL). Pro optimalizaci sítě umožňuje funkce Automatického sousedního vztahu (ANR) síti automaticky objevovat NCELLy na základě hlášení od UE, čímž se snižuje potřeba ruční konfigurace. Vztah NCELL je také klíčový pro koordinaci interference (eICIC, FeICIC), kde koordinace vysílacích vzorů mezi obslužnou a sousedními buňkami může zmírnit interferenci, zejména na okrajích buněk.

## K čemu slouží

Koncept sousední buňky existuje k vyřešení základní výzvy mobility v celulární síti: udržení nepřetržitého a kvalitního komunikačního spojení pro uživatele pohybujícího se přes geografické oblasti pokryté diskrétními lokalitami buněk. Bez znalosti a správy NCELLů by se spojení UE jednoduše přerušilo, když by zařízení opustilo dosah své obslužné buňky. Rámec NCELL umožňuje proaktivní, sítí řízenou mobilitu. Identifikací a monitorováním potenciálních cílových buněk dříve, než se spojení s obslužnou buňkou kriticky zhorší, může síť orchestrovat plynulé předání spojení a minimalizovat přerušení služby.

Historicky byly v raných celulárních systémech seznamy sousedů staticky konfigurovány operátory sítí, což bylo pracné a náchylné k chybám, zejména s tím, jak sítě houstly a stávaly se složitějšími. Vývoj směrem k Automatickému sousednímu vztahu (ANR) v LTE a NR to řešil tím, že umožnil UE detekovat a hlásit neznámé buňky, které síť mohla následně přidat do své NRT. Tato dynamická správa je nezbytná pro moderní heterogenní sítě (HetNets) s malými buňkami, kde se rádiové prostředí často mění. Koncept NCELL také podporuje pokročilé funkce jako vyrovnávání zatížení, kde lze provoz přesunout na méně vytížené sousední buňky, a úsporu energie, kde mohou být buňky vypínány během období nízkého provozu přesunutím uživatelů na NCELLy.

## Klíčové vlastnosti

- Kandidátní buňka pro procedury předání spojení (handover) nebo převýběru buňky
- Identifikována jedinečnými identifikátory buňky (PCI, CGI/ECGI)
- Uvedena v Tabulce sousedních vztahů (NRT) obslužné buňky
- UE měří NCELLy na základě síťově nakonfigurovaných měřicích objektů
- Podporuje mobilitu v rámci kmitočtu, mezi kmitočty a mezi různými RAT
- Spravována dynamicky pomocí funkce Automatického sousedního vztahu (ANR)

## Související pojmy

- [PCI – Physical Cell Identity](/mobilnisite/slovnik/pci/)
- [ANR – Automatic Neighbour Relationship](/mobilnisite/slovnik/anr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [NCELL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncell/)
