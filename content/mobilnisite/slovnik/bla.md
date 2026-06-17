---
slug: "bla"
url: "/mobilnisite/slovnik/bla/"
type: "slovnik"
title: "BLA – Broken Link Access"
date: 2025-01-01
abbr: "BLA"
fullName: "Broken Link Access"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bla/"
summary: "Broken Link Access (BLA) je mechanismus 3GPP, který umožňuje uživatelskému zařízení (UE) získat přístup k síťovým prostředkům, když je primární rádiové spojení narušeno nebo nedostupné. Poskytuje alte"
---

BLA je mechanismus 3GPP, který umožňuje uživatelskému zařízení (UE) získat přístup k síťovým prostředkům pomocí alternativních metod, když je primární rádiové spojení narušeno nebo nedostupné, za účelem zachování kontinuity služeb.

## Popis

Broken Link Access (BLA) je standardizovaný mechanismus ve specifikacích 3GPP, který řeší scénáře, kdy je primární rádiové spojení mezi uživatelským zařízením (UE) a sítí narušeno, degradováno nebo zcela nedostupné. Architektura zahrnuje úpravy jak v chování UE, tak v síťových prvcích za účelem detekce stavů selhání spojení a zahájení alternativních přístupových procedur. Když UE detekuje, že je její primární rádiové spojení přerušeno nebo silně degradováno pod použitelné prahové hodnoty, spustí procedury BLA ve snaze znovu navázat konektivitu prostřednictvím dostupných alternativních prostředků.

Technicky BLA funguje prostřednictvím vícefázového procesu zahrnujícího detekci, vyhodnocení a obnovu. UE kontinuálně monitoruje klíčové indikátory kvality rádiového spojení, jako je Reference Signal Received Power (RSRP), Reference Signal Received Quality (RSRQ) a Block Error Rate ([BLER](/mobilnisite/slovnik/bler/)). Když tyto metriky poklesnou pod předdefinované prahové hodnoty po delší dobu, UE vyhlásí stav přerušeného spojení. UE poté vyhodnotí dostupné alternativní možnosti přístupu, které mohou zahrnovat přepnutí na jiné kmitočtové pásmo, pokus o přístup přes sousední buňky nebo využití jiné rádiové přístupové technologie (RAT), pokud je podporována více-RAT schopnost.

Klíčové síťové komponenty zapojené do BLA zahrnují vrstvu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) pro správu stavů spojení, vrstvu Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) pro plánování a alokaci prostředků a fyzickou vrstvu (PHY) pro skutečný přenos a příjem signálu. Síťová strana musí BLA podporovat tím, že udržuje kontextovou informaci pro UE, která zažívají selhání spojení, a je připravena zpracovávat pokusy o přístup přes alternativní cesty. To vyžaduje koordinaci mezi obsluhující a cílovou buňkou, potenciálně zahrnující rozhraní X2 pro komunikaci mezi buňkami v LTE nebo rozhraní Xn v 5G NR.

Implementace BLA se liší v závislosti na konkrétním scénáři a konfiguraci sítě. V některých případech může zahrnovat procedury převýběru buňky s prioritním zacházením pro UE ve stavu přerušeného spojení. V jiných implementacích může spustit procedury náhodného přístupu (RACH) s modifikovanými parametry pro zvýšení pravděpodobnosti přístupu. Mechanismus také zohledňuje aspekty úspory energie, protože UE ve stavu přerušeného spojení mohou potřebovat šetřit baterii během pokusů o obnovu. Úspěšné provedení BLA vede k opětnému navázání konektivity UE, potenciálně se sníženou kvalitou služby, dokud nemohou být obnoveny optimální podmínky.

## K čemu slouží

BLA byl zaveden, aby řešil kritické mezery ve spolehlivosti mobilních sítí, zejména pro aplikace vyžadující vysokou dostupnost, jako jsou komunikace pro veřejnou bezpečnost, průmyslová automatizace a síťové aplikace v dopravě. Před standardizací BLA předpokládaly síťové přístupové procedury relativně stabilní rádiové podmínky, přičemž mechanismy obnovy byly navrženy primárně pro úplnou ztrátu spojení spíše než pro postupnou degradaci spojení. To činilo UE zranitelnými vůči přerušení služeb během částečných selhání spojení, kdy se tradiční procedury předávání spojení (handover) nebo opětovného připojení nemusely správně aktivovat.

Historický kontext vývoje BLA zahrnuje rostoucí nasazování služeb s požadavkem na vysokou dostupnost (mission-critical) přes buněčné sítě, kde by mohlo mít i dočasné přerušení služby vážné následky. Tradiční buněčné systémy optimalizované pro spotřebitelské aplikace mohly tolerovat krátké výpadky konektivity, ale nové případy užití v oblastech jako chytré sítě, vzdálená zdravotní péče a autonomní systémy vyžadovaly robustnější přístupové mechanismy. BLA tuto mezeru zaplňuje tím, že poskytuje standardizované procedury pro detekci a obnovu z degradace spojení dříve, než dojde k úplné ztrátě připojení.

Předchozí přístupy ke spolehlivosti spojení se primárně zaměřovaly na optimalizaci předávání spojení (handover) a opětovné navázání spojení po úplném selhání. Tyto metody často selhávaly ve scénářích, kde se spojení postupně nebo přerušovaně degradovalo, protože UE nemusela splňovat kritéria pro handover, přestože zažívala nepřijatelnou kvalitu služby. BLA tuto limitaci řeší zavedením podrobnějšího hodnocení kvality spojení a proaktivních mechanismů obnovy, které se mohou aktivovat dříve, než se spojení stane zcela nepoužitelným, čímž se zlepšuje celková spolehlivost systému a uživatelský zážitek.

## Klíčové vlastnosti

- Kontinuální monitorování kvality rádiového spojení s konfigurovatelnými prahovými hodnotami
- Mechanismy pro vyhodnocení a výběr alternativní přístupové cesty
- Modifikované procedury náhodného přístupu (RACH) pro zvýšení pravděpodobnosti úspěchu
- Podpora přechodu na jinou RAT (Multi-RAT fallback), pokud je dostupná
- Zachování síťového kontextu během obnovy spojení
- Provoz s nízkou spotřebou energie během stavu přerušeného spojení

## Definující specifikace

- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [BLA na 3GPP Explorer](https://3gpp-explorer.com/glossary/bla/)
